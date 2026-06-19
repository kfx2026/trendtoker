const fs = require('fs');
const vm = require('vm');

const file = 'index.html';
const h = fs.readFileSync(file, 'utf-8');

// Extract script blocks with their line numbers
const lines = h.split('\n');
const re = /<script([^>]*)>([\s\S]*?)<\/script>/gi;
let allOk = true;
let m;
let blockNum = 0;

while ((m = re.exec(h)) !== null) {
  blockNum++;
  const attrs = m[1];
  const code = m[2].trim();
  
  // Skip JSON-LD
  if (attrs.includes('application/ld+json') || attrs.includes('application/json')) {
    console.log(`Block ${blockNum}: SKIP (JSON-LD)`);
    continue;
  }
  
  if (!code) {
    console.log(`Block ${blockNum}: SKIP (empty)`);
    continue;
  }
  
  // Find line number
  const beforeCode = h.substring(0, m.index);
  const lineNum = beforeCode.split('\n').length;
  
  try {
    new vm.Script(code);
    console.log(`Block ${blockNum} (line ~${lineNum}): OK`);
  } catch (e) {
    console.log(`Block ${blockNum} (line ~${lineNum}): FAIL — ${e.message}`);
    // Show some context around the error
    const errorLines = code.split('\n');
    console.log(`  Code length: ${code.length} chars, ${errorLines.length} lines`);
    allOk = false;
  }
}

if (allOk) {
  console.log('\nAll OK!');
  process.exit(0);
} else {
  process.exit(1);
}
