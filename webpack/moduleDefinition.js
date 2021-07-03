module.exports = {
  rules: [
    {
      test: /\.jsx?$/,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader',
      },
    },
    {
      test: /\.css$/,
      use: [
        {
          loader: 'style-loader',
          options: {
            insertAt: 'top',
          },
        },
        {
          loader: 'css-loader',
        },
      ],
    },
  ],
};
