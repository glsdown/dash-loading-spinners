import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import {RiseLoader} from 'react-spinners';
import CoveringContainer from '../../private/CoveringContainer.react';

/**
 * Five dots which alternately rise up and down, increasing and decreasing
 * in size as they do.
 */
const Rise = (props) => {
  const {
    children,
    color,
    loading_state,
    fullscreenClassName,
    fullscreen_style,
    fullscreen,
    debounce,
    show_initially,
    width,
    speed_multiplier,
  } = props;

  // Loading options
  const [showSpinner, setShowSpinner] = useState(show_initially);
  const timer = useRef();

  const margin = 2;
  const size = Math.floor((width - 6 * margin) / 3);

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
    <RiseLoader
      color={color}
      size={size}
      margin={margin}
      speedMultiplier={speed_multiplier}
    />
  );

  return (
    <CoveringContainer
      children={children}
      fullscreenClassName={fullscreenClassName}
      fullscreen_style={fullscreen_style}
      fullscreen={fullscreen}
      minHeight={size * 2 + 4 * margin}
      minWidth={width}
      SpinnerDiv={SpinnerDiv}
      showSpinner={showSpinner}
    />
  );
};

Rise._dashprivate_isLoadingComponent = true;

Rise.defaultProps = {
  debounce: 0,
  show_initially: true,
  color: '#000000',
  speed_multiplier: 1,
  width: 57,
};

Rise.propTypes = {
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
   * Defines CSS styles for the container.
   */
  fullscreen_style: PropTypes.object,

  /**
   * CSS class names to apply to the container.
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
   * The relative speed of the spinner
   */
  speed_multiplier: PropTypes.number,

  /**
   * The spinner width (in px)
   */
  width: PropTypes.number,

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

export default Rise;
