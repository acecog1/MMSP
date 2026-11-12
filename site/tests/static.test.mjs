import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
const html=readFileSync(new URL('../index.html',import.meta.url),'utf8');
test('portal contains all thirteen Temple names',()=>{
 const names=['Origin','Breath','Waters','Earth','Fire','the Heart','Voice','Light','Shadow','Time','Dream','Star','Return'];
 for(const name of names)assert.ok(html.includes('"'+name+'"'),name);
});
test('portal has intentional accessibility and privacy cues',()=>{
 for(const phrase of ['lang="en"','name="viewport"','aria-label="Main navigation"','role="status"','localStorage','Demonstration only'])assert.ok(html.includes(phrase),phrase);
});
test('portal distinguishes simulated recognition',()=>assert.ok(html.includes('not a credential, graduation, or institutional approval')));
test('portal has no external script or network usage',()=>{
 assert.ok(!/<script[^>]*src=/i.test(html));
 assert.ok(!/\b(fetch|XMLHttpRequest|WebSocket)\s*\(/.test(html));
});
