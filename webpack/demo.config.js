const path = require('path');

const packagejson = require('../package.json');
const directories = require('./directories');
const moduleDefinition = require('./moduleDefinition');

BUILD_PATH = path.join(directories.ROOT, 'demo-lib');

const dashLibraryName = packagejson.name.replace(/-/g, '_');

module.exports = (env, argv) => {
  let mode;

  const overrides = module.exports || {};

  // if user specified mode flag take that value
  if (argv && argv.mode) {
    mode = argv.mode;
  }

  // else if configuration object is already set (module.exports) use that value
  else if (overrides.mode) {
    mode = overrides.mode;
  }

  // else take webpack default (production)
  else {
    mode = 'production';
  }

  return {
    mode,
    entry: {
      bundle: [path.join(directories.DEMO, 'index.js')],
    },
    output: {
      path: BUILD_PATH,
      filename: "dash_loading_spinners.js",
      library: dashLibraryName,
      libraryTarget: 'this',
      pathinfo: true,
      publicPath: '/demo-lib/',
    },
    module: moduleDefinition,
    devServer: {
      contentBase: directories.DEMO,
      compress: true,
      port: 9000,
    },
  };
};
