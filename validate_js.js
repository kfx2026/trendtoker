const fs = require('fs');
const vm = require('vm');

const files = ['china', 'us', 'eu', 'article', 'index'];
let allOk = true;

files.forEach(function(n) {
  const h = fs.readFileSync(n + '.html', 'utf-8');
  const re = /<script[^>]*>([\s\S]*?)<\/script>/gi;
  let ok = true;
  let m;
  while ((m = re.exec(h)) !== null) {
    const code = m[1].trim();
    // Skip JSON-LD and empty scripts
    if (!code || code.includes('application/ld+json') || code.includes('application/json')) continue;
    try {
      new vm.Script(code);
    } catch (e) {
      console.log('JS ERROR in ' + n + '.html: ' + e.message);
      ok = false;
    }
  }
  if (ok) {
    console.log(n + '.html: OK');
  } else {
    console.log(n + '.html: FAIL');
    allOk = false;
  }
});

if (!allOk) {
  process.exit(1);
} else {
  console.log('\nAll HTML files passed JS validation.');
}
