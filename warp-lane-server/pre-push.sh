SRC_PATTERN="warp-lane-server"
if git diff --cached --name-only | grep --quiet "$SRC_PATTERN"
then
  # TODO
  #ng lint && ng test --watch=false
fi
  echo "none"
  exit 0