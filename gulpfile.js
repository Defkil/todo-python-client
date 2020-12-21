const {src, dest, watch, series} = require('gulp'),
    pug = require('gulp-pug'),
    sass = require('gulp-sass'),
    exec = require('child_process').exec,
    del = require('del'),
    { join } = require('path')

const JS_DEPENDENCIES = [
    './node_modules/bootstrap/dist/js/bootstrap.min.js',
    './node_modules/bootstrap/dist/js/bootstrap.min.js.map',
    './node_modules/jquery/dist/jquery.min.js'
]

const DIR_SRC = 'src/',
    DIR_DIST = 'dist/',
    DIR_APP = join(DIR_SRC, 'app')

const SRC_PY_BLOB = join(DIR_APP, '**/*.py'),
    SRC_PUG_FILE = join(DIR_SRC, 'views/index.pug').replace(/\\/g, '/'),
    SRC_PUG_BLOB = join(DIR_SRC, 'views/**/*.pug'),
    SRC_SASS_FILE = join(DIR_SRC, 'style/style.scss').replace(/\\/g, '/'),
    SRC_SASS_BLOB = join(DIR_SRC, 'style/**/*.scss'),
    SRC_LIB_BLOB = join(DIR_SRC, 'libs/**/*.*').replace(/\\/g, '/'),
    SRC_ASSETS_BLOB = join(DIR_SRC, 'assets/**/*.*').replace(/\\/g, '/')

const BRYTHON_CLI_CMD = 'brython-cli --make_package todoApp',
    BRYTHON_BUILD_FILE = join(DIR_APP, 'todoApp.brython.js').replace(/\\/g, '/')

/**
 * Render pug files
 *
 * @returns {*} Gulp pipe
 */
function pugScript() {
    console.log(SRC_PUG_FILE)
  return src(SRC_PUG_FILE)
    .pipe(pug()).pipe(dest(DIR_DIST))
}

/**
 * Build Sass files
 *
 * @returns {*} Gulp pipe
 */
function sassScript() {
  return src(SRC_SASS_FILE)
      .pipe(sass({includePaths: ['node_modules']}).on('error', sass.logError))
      .pipe(dest(DIR_DIST))
}

/**
 * Move dependencies
 *
 * @returns {*} Gulp pipe
 */
function moveLibJsScript() {
  return src([SRC_LIB_BLOB, ...JS_DEPENDENCIES]).pipe(dest(DIR_DIST))
}

/**
 * Run Brython CLI command
 *
 * @param cb finish callback
 */
function runBrython(cb) {
    exec(BRYTHON_CLI_CMD, {cwd: DIR_APP}, cb)
}

/**
 * Move Brython build to destination folder
 *
 * @returns {*} Gulp pipe
 */
function moveBrython() {
    return src(BRYTHON_BUILD_FILE).pipe(dest(DIR_DIST))
}

/**
 * Cleanup Brython build
 *
 * @param cb finish callback
 */
function cleanBrython(cb) {
    del.sync([BRYTHON_BUILD_FILE])
    cb()
}

/**
 * Move assets to destination folder
 *
 * @returns {*} Gulp pipe
 */
function moveAssetsScript() {
  return src(SRC_ASSETS_BLOB).pipe(dest(DIR_DIST))
}

const buildBrython = series(runBrython, moveBrython, cleanBrython)
const moveScripts = series(moveLibJsScript, moveAssetsScript, buildBrython);
const build = series(pugScript, moveScripts, sassScript)

function watchScript() {
  build()
  watch([SRC_PUG_BLOB], pugScript);
  watch([SRC_LIB_BLOB], moveLibJsScript);
  watch([SRC_PY_BLOB, '!' + BRYTHON_BUILD_FILE], buildBrython);
  watch([SRC_ASSETS_BLOB], moveAssetsScript);
  watch([SRC_SASS_BLOB], sassScript);
}

exports.sass = sassScript
exports.pug = pugScript
exports.watch = watchScript
exports.move = moveScripts
exports.build = build