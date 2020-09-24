SRC_PATTERN="warp-lane-ng-client"
if git diff --cached --name-only | grep --quiet "$SRC_PATTERN"
then
  ng lint && ng test --watch=false
fi
  echo "none"
  exit 0