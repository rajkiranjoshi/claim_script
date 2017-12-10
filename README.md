# claim_script

Note in claim-cs1010x-ay1516s2.js, the line `$.getScript(core_script)` will only work correctly if jquery is included. Now jquery can be easily included using a plugin like [Javascript Library for Console](https://chrome.google.com/webstore/detail/javascript-library-for-co/hoooohdeiheekoemicbaeeiaokjhnpko)

## Steps
1. Use `generate_js.py` to first generate the javascript code from your input csv, to be plugged into `claim-cs1010x-ay1516s2.js`.
2. Make sure you are on https://mysoc.nus.edu.sg/~tssclaim/tutor/teach_claim.php page and the aforementioned plugin is configured to load jquery.
3. Now, open the javascript console of your browser and copy-paste entire `claim-cs1010x-ay1516s2.js` with the newly plugged-in code. Enter info in the prompts. After that on console, call the function `c.makeAllClaims();`. Be patient as this might take some time. Note that the function call `c.makeAllClaims();` this is currently commented in `claim-cs1010x-ay1516s2.js`.
