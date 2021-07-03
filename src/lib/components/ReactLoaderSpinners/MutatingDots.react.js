import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import CoveringContainer from '../../private/CoveringContainer.react';

/**
 * Two dots (optionally of different colours) morphing and rotating around
 * a central point.
 */
const MutatingDots = (props) => {
  const {
    id,
    children,
    color,
    secondaryColor,
    loading_state,
    fullscreenClassName,
    fullscreen_style,
    fullscreen,
    debounce,
    show_initially,
    height,
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

  const SpinnerDiv = () => (
    <svg id="goo-loader" width={width} height={height} aria-label="loading">
      <filter id="fancy-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="blur" />
        <feColorMatrix
          in="blur"
          mode="matrix"
          values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 19 -9"
          result="goo"
        />
        <feComposite in="SourceGraphic" in2="goo" operator="atop" />
      </filter>
      <g filter="url(#fancy-goo)">
        <animateTransform
          id="mainAnim"
          attributeName="transform"
          attributeType="XML"
          type="rotate"
          from={`0 ${Math.ceil(width / 2)} ${Math.ceil(height / 2)}`}
          to={`360 ${Math.ceil(width / 2)} ${Math.ceil(height / 2)}`}
          dur="1.2s"
          repeatCount="indefinite"
        />
        <circle cx="50%" cy={`${Math.ceil(width / 2)}`} r={radius} fill={color}>
          <animate
            id="cAnim1"
            attributeType="XML"
            attributeName="cy"
            dur="0.6s"
            begin="0;cAnim1.end+0.2s"
            calcMode="spline"
            values={`${Math.ceil(width / 2)};${Math.ceil(
              width / 4
            )};${Math.ceil(width / 2)}`}
            keyTimes="0;0.3;1"
            keySplines="0.09, 0.45, 0.16, 1;0.09, 0.45, 0.16, 1"
          />
        </circle>
        <circle
          cx="50%"
          cy="75%"
          r={radius}
          fill={secondaryColor ? secondaryColor : color}
        >
          <animate
            id="cAnim2"
            attributeType="XML"
            attributeName="cy"
            dur="0.6s"
            begin="0.4s;cAnim2.end+0.2s"
            calcMode="spline"
            values={`${3 * Math.ceil(width / 4)};${height - radius};${
              3 * Math.ceil(width / 4)
            }`}
            keyTimes="0;0.3;1"
            keySplines="0.09, 0.45, 0.16, 1;0.09, 0.45, 0.16, 1"
          />
        </circle>
      </g>
    </svg>
  );

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

MutatingDots._dashprivate_isLoadingComponent = true;

MutatingDots.defaultProps = {
  debounce: 0,
  show_initially: true,
  color: '#000000',
  width: 80,
  height: 80,
  radius: 11,
};

MutatingDots.propTypes = {
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
   * The spinner height (in px)
   */
  height: PropTypes.number,

  /**
   * The spinner width (in px)
   */
  width: PropTypes.number,

  /**
   * The radius of the dots (in px)
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

export default MutatingDots;
