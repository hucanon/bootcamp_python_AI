

set -ex



test -f "${PREFIX}/include/yaml.h"
test -f "${PREFIX}/lib/libyaml.a"
test -f "${PREFIX}/lib/libyaml.dylib"
exit 0
