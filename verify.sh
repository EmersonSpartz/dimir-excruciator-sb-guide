#!/usr/bin/env bash
set -e
URL="https://emersonspartz.github.io/dimir-excruciator-sb-guide/"
html=$(curl -sf "$URL")
for n in "Doomsday Excruciator" "Your grid" "pre-ban" "Kavaero" "Requiting Hex" "off by"; do
  grep -q "$n" <<< "$html" || { echo "FAIL: missing '$n'"; exit 1; }
done
mus=$(grep -o '<div class="mu\( open\)\?">' <<< "$html" | wc -l | tr -d ' ')
[ "$mus" -ge 17 ] || { echo "FAIL: expected >=17 sections, got $mus"; exit 1; }
echo "PASS: $mus sections, all key strings present"
