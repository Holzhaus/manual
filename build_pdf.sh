#!/bin/sh

# Parse languages
cd source || exit 1
VERSION="$(python -c 'import conf; print(conf.version)')"
LANGUAGES="$(python -c 'import conf; print(" ".join(sorted((lang for lang in conf.supported_languages.keys()), reverse=True)))')"
cd .. || exit 1
NUM_LANGUAGES="$(printf '%s' "$LANGUAGES" | wc -w)"

printf 'Building %d languages: %s\n' "$NUM_LANGUAGES" "$LANGUAGES"

mkdir -p build/pdf

i=1
for lang in $LANGUAGES
do
    printf -- '::group::Language %s [%d/%d]\n' "$lang" "$i" "$NUM_LANGUAGES"

    SPHINXOPTS="-q -j $(nproc) -Dlanguage=${lang}"
    LATEXMKOPTS="-f -interaction=nonstopmode -pdf"
    BUILDDIR="build/latex/${lang}"

    if [ "${lang}" = "ja-JP" ]
    then
        SPHINXOPTS="${SPHINXOPTS} -Dlatex_engine=platex"
    elif [ "${lang}" = "zh-CN" ] || [ "${lang}" = "zh-TW" ]
    then
        SPHINXOPTS="${SPHINXOPTS} -Dlatex_engine=xelatex -Dlatex_elements.preamble=\\usepackage[UTF8]{ctex}\\n"
        LATEXMKOPTS="${LATEXMKOPTS} -xelatex"
    else
        SPHINXOPTS="${SPHINXOPTS} -Dlatex_engine=xelatex"
        LATEXMKOPTS="${LATEXMKOPTS} -xelatex"
    fi

    sphinx-build -b latex source "${BUILDDIR}" ${SPHINXOPTS}
    make -C "${BUILDDIR}" LATEXMKOPTS="${LATEXMKOPTS}" all-pdf >/dev/null
    [ -e "${BUILDDIR}/Mixxx-Manual.pdf" ] && cp "${BUILDDIR}/Mixxx-Manual.pdf" "build/pdf/mixxx-manual-${VERSION}-${lang}.pdf"
    i=$((i + 1))

    printf -- '::endgroup::'
done
