#!/bin/sh
cd "source"
export VERSION="$(python -c 'import conf; print(conf.version)')"
export LANGUAGES="$(python -c 'import conf; print(" ".join(sorted((lang for lang in conf.supported_languages.keys()), reverse=True)))')"
cd ..
for language in ${LANGUAGES};
do
  mkdir -p "build/qthelp/lang/${language}"
  sphinx-build -b qthelp -d "build/qthelp/.doctrees" -a -j auto "-Dqthelp_basename=manual-${language}" "-Dlanguage=${language}" source "build/qthelp/lang/${language}"
done
mkdir -p "build/qthelp/multilang"
tools/qthelp.py "build/qthelp/lang" "build/qthelp/multilang"
mkdir -p "deploy/manual/${version}"
mv "build/qthelp/multilang/manual.qhc" "deploy/manual/${version}/mixxx-manual.qhc"
