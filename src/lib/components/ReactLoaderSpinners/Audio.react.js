import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
// import Loader from 'react-loader-spinner';
// import 'react-loader-spinner/dist/loader/css/react-spinner-loader.css';
import CoveringContainer from '../../private/CoveringContainer.react';

/**
 * Audio bars beating spinner.
 */
const Audio = (props) => {
  const {
    id,
    children,
    color,
    loading_state,
    fullscreenClassName,
    fullscreen_style,
    fullscreen,
    debounce,
    show_initially,
    height,
    width,
    thickness,
  } = props;

  // Loading options
  const [showSpinner, setShowSpinner] = useState(show_initially);
  const timer = useRef();

  useEffect(() => {
    if (loading_state) {
      if (timer.current) {
        clearTimeout(timer.current);
      }
      if (loading_state.is_loading && !showSpinner) {
        setShowSpinner(true);
      } else if (!loading_state.is_loading && showSpinner) {
        timer.current = setTimeout(() => setShowSpinner(false), debounce);
      }
    }
  }, [loading_state]);

  const SpinnerDiv = () => {
    const original_height = 80;
    return (
      <svg
        height={height}
        width={width}
        fill={color}
        viewBox={`0 0 ${width} ${height}`}
        xmlns="http://www.w3.org/2000/svg"
        aria-label="loading"
      >
        <g transform={`matrix(1 0 0 -1 0 ${height})`}>
          <rect width={`${thickness}`} height="25%" rx="3">
            <animate
              attributeName="height"
              begin="0s"
              dur="4.3s"
              // values="20;45;57;80;64;32;66;45;64;23;66;13;64;56;34;34;2;23;76;79;20"
              values={`${Math.ceil(
                (height * 20) / original_height
              )};${Math.ceil((height * 45) / original_height)}; ${Math.ceil(
                (height * 57) / original_height
              )};${Math.ceil((height * 80) / original_height)};${Math.ceil(
                (height * 64) / original_height
              )};${Math.ceil((height * 32) / original_height)};${Math.ceil(
                (height * 66) / original_height
              )};${Math.ceil((height * 45) / original_height)};${Math.ceil(
                (height * 64) / original_height
              )};${Math.ceil((height * 23) / original_height)};${Math.ceil(
                (height * 66) / original_height
              )};${Math.ceil((height * 13) / original_height)};${Math.ceil(
                (height * 64) / original_height
              )}; ${Math.ceil((height * 56) / original_height)};${Math.ceil(
                (height * 34) / original_height
              )};${Math.ceil((height * 34) / original_height)};${Math.ceil(
                (height * 2) / original_height
              )};${Math.ceil((height * 23) / original_height)};${Math.ceil(
                (height * 76) / original_height
              )};${Math.ceil((height * 79) / original_height)};${Math.ceil(
                (height * 20) / original_height
              )}`}
              calcMode="linear"
              repeatCount="indefinite"
            />
          </rect>
          <rect
            x={`${Math.ceil(thickness * 1.5)}`}
            width={`${thickness}`}
            height="100%"
            rx="3"
          >
            <animate
              attributeName="height"
              begin="0s"
              dur="2s"
              values={`${height};${Math.ceil(
                (height * 55) / original_height
              )};${Math.ceil((height * 33) / original_height)}; ${Math.ceil(
                (height * 5) / original_height
              )};${Math.ceil((height * 75) / original_height)};${Math.ceil(
                (height * 23) / original_height
              )};${Math.ceil((height * 73) / original_height)};${Math.ceil(
                (height * 33) / original_height
              )};${Math.ceil((height * 12) / original_height)};${Math.ceil(
                (height * 14) / original_height
              )};${Math.ceil((height * 60) / original_height)};${height}`}
              calcMode="linear"
              repeatCount="indefinite"
            />
          </rect>
          <rect
            x={`${2 * Math.ceil(thickness * 1.5)}`}
            width={`${thickness}`}
            height={`${Math.ceil((height * 50) / original_height)}`}
            rx="3"
          >
            <animate
              attributeName="height"
              begin="0s"
              dur="1.4s"
              values={`${Math.ceil(
                (height * 50) / original_height
              )};${Math.ceil((height * 34) / original_height)}; ${Math.ceil(
                (height * 78) / original_height
              )};${Math.ceil((height * 23) / original_height)};${Math.ceil(
                (height * 56) / original_height
              )};${Math.ceil((height * 23) / original_height)};${Math.ceil(
                (height * 34) / original_height
              )};${Math.ceil((height * 76) / original_height)};${Math.ceil(
                (height * 80) / original_height
              )};${Math.ceil((height * 54) / original_height)};${Math.ceil(
                (height * 21) / original_height
              )};${Math.ceil((height * 50) / original_height)}`}
              calcMode="linear"
              repeatCount="indefinite"
            />
          </rect>
          <rect
            x={`${3 * Math.ceil(thickness * 1.5)}`}
            width={`${thickness}`}
            height={`${Math.ceil((height * 30) / original_height)}`}
            rx="3"
          >
            <animate
              attributeName="height"
              begin="0s"
              dur="2s"
              values={`${Math.ceil(
                (height * 30) / original_height
              )};${Math.ceil((height * 45) / original_height)}; ${Math.ceil(
                (height * 13) / original_height
              )};${Math.ceil((height * 80) / original_height)};${Math.ceil(
                (height * 56) / original_height
              )};${Math.ceil((height * 72) / original_height)};${Math.ceil(
                (height * 45) / original_height
              )};${Math.ceil((height * 76) / original_height)};${Math.ceil(
                (height * 34) / original_height
              )};${Math.ceil((height * 23) / original_height)};${Math.ceil(
                (height * 67) / original_height
              )};${Math.ceil((height * 30) / original_height)}`}
              calcMode="linear"
              repeatCount="indefinite"
            />
          </rect>
        </g>
      </svg>
    );
  };

  return (
    <CoveringContainer
      id={id}
      children={children}
      fullscreen={fullscreen}
      fullscreenClassName={fullscreenClassName}
      fullscreen_style={fullscreen_style}
      minHeight={height}
      minWidth={width}
      SpinnerDiv={SpinnerDiv}
      showSpinner={showSpinner}
    />
  );
};

Audio._dashprivate_isLoadingComponent = true;

Audio.defaultProps = {
  debounce: 0,
  show_initially: true,
  color: '#000000',
  width: 80,
  height: 80,
  thickness: 10,
};

Audio.propTypes = {
  /**
   * The ID of this component, used to identify dash components
   * in callbacks. The ID needs to be unique across all of the
   * components in an app.
   */
  id: PropTypes.string,

  /**
   * The children of this component.
   */
  children: PropTypes.node,

  /**
   * Defines CSS styles for the container when in fullscreen.
   */
  fullscreen_style: PropTypes.object,

  /**
   * CSS class names to apply to the container when in fullscreen.
   */
  fullscreenClassName: PropTypes.string,

  /**
   * Sets the color of the Spinner. You can also specify any valid CSS color
   * of your choice (e.g. a hex code, a decimal code or a CSS color name).
   *
   * If not specified will default to black.
   */
  color: PropTypes.string,

  /**
   * The spinner height (in px)
   */
  height: PropTypes.number,

  /**
   * The spinner width (in px)
   */
  width: PropTypes.number,

  /**
   * The thickness of the bars (in px). The gaps between the bars will be
   * half the thickness of the bar itself.
   */
  thickness: PropTypes.number,

  /**
   * Boolean that determines if the loading spinner will be displayed
   * full-screen or not.
   */
  fullscreen: PropTypes.bool,

  /**
   * When using the spinner as a loading spinner, add a time delay (in ms) to
   * the spinner being removed to prevent flickering.
   */
  debounce: PropTypes.number,

  /**
   * Whether the Spinner should show on app start-up before the loading state
   * has been determined. Default True.
   */
  show_initially: PropTypes.bool,
};

export default Audio;
