SRC_PATTERN="warp-lane-ng-client"
if git diff --cached --name-only | grep --quiet "$SRC_PATTERN"
then
  ng e2e && ng test --watch=false && ng build --aot true
fi
  echo "none"
  exit 0
  