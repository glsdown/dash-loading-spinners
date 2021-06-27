import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import CoveringContainer from '../../private/CoveringContainer.react';

/**
 * Solid circle (optionally of a different colour) rotating around a
 * faded ring.
 */
const RevolvingDot = (props) => {
  const {
    children,
    color,
    secondaryColor,
    speedMultiplier,
    loading_state,
    fullscreenClassName,
    fullscreen_style,
    fullscreen,
    debounce,
    show_initially,
    width,
    radius,
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
    const animationTime = 2 / speedMultiplier;
    return (
      <svg
        version="1.1"
        width={width}
        height={width}
        xmlns="http://www.w3.org/2000/svg"
        x="0px"
        y="0px"
        aria-label="loading"
      >
        <circle
          fill="none"
          stroke={color}
          strokeWidth={Math.ceil(radius / 3)}
          cx={Math.ceil(width / 2)}
          cy={Math.ceil(width / 2)}
          r={Math.ceil(width / 2) - 2 * radius}
          style={{opacity: 0.5}}
        />
        <circle
          fill={secondaryColor ? secondaryColor : color}
          stroke={secondaryColor ? secondaryColor : color}
          strokeWidth="3"
          cx={Math.ceil(width / 2)}
          cy={radius * 2}
          r={radius}
        >
          <animateTransform
            attributeName="transform"
            dur={`${animationTime}s`}
            type="rotate"
            from={`0 ${Math.ceil(width / 2)} ${Math.ceil(width / 2)}`}
            to={`360 ${Math.ceil(width / 2)} ${Math.ceil(width / 2)}`}
            repeatCount="indefinite"
          />
        </circle>
      </svg>
    );
  };

  return (
    <CoveringContainer
      children={children}
      fullscreen={fullscreen}
      fullscreenClassName={fullscreenClassName}
      fullscreen_style={fullscreen_style}
      minHeight={width}
      minWidth={width}
      SpinnerDiv={SpinnerDiv}
      showSpinner={showSpinner}
    />
  );
};

RevolvingDot._dashprivate_isLoadingComponent = true;

RevolvingDot.defaultProps = {
  debounce: 0,
  show_initially: true,
  color: '#000000',
  speedMultiplier: 1,
  width: 80,
  radius: 6,
};

RevolvingDot.propTypes = {
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
   * Sets the color of the Spinner. You can also specify any valid CSS color
   * of your choice (e.g. a hex code, a decimal code or a CSS color name).
   *
   * If not specified will default to blue.
   */
  secondaryColor: PropTypes.string,

  /**
   * The relative speed of the spinner
   */
  speedMultiplier: PropTypes.number,

  /**
   * The spinner width (in px)
   */
  width: PropTypes.number,

  /**
   * The radius of the spinning dot (in px)
   */
  radius: PropTypes.number,

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

export default RevolvingDot;
