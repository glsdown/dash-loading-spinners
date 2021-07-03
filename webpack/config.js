const path = require('path');
const packagejson = require('../package.json');
const moduleDefinition = require('./moduleDefinition');

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

  let filename = (overrides.output || {}).filename;
  if (!filename) {
    const modeSuffix = mode === 'development' ? 'dev' : 'min';
    filename = `${dashLibraryName}.${modeSuffix}.js`;
  }

  const entry = overrides.entry || {main: './src/lib/index.js'};
  const devtool = overrides.devtool || 'source-map';

  const externals =
    'externals' in overrides
      ? overrides.externals
      : {
          react: 'React',
          'react-dom': 'ReactDOM',
          'plotly.js': 'Plotly',
          'prop-types': 'PropTypes',
        };

  return {
    mode,
    entry,
    output: {
      path: path.resolve(__dirname, '..', dashLibraryName),
      filename,
      library: dashLibraryName,
      libraryTarget: 'window',
    },
    devtool,
    externals,
    module: moduleDefinition,
    devServer: {
      contentBase: path.join(__dirname, '..', 'src', 'demo'),
      compress: true,
      port: 9000,
    },
  };
};
