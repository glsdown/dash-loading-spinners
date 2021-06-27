import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import {GridLoader} from 'react-spinners';
import CoveringContainer from '../../private/CoveringContainer.react';

/**
 * Nine dots arranged in a grid pattern, shrinking and growing at different times.
 */
const Grid = (props) => {
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
    margin,
    speed_multiplier,
  } = props;

  // Loading options
  const [showSpinner, setShowSpinner] = useState(show_initially);
  const timer = useRef();

  const size = Math.floor((width - 3 * margin) / 3);

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
    <GridLoader
      color={color}
      size={size}
      margin={Math.floor(margin / 2)}
      speedMultiplier={speed_multiplier}
    />
  );

  return (
    <CoveringContainer
      children={children}
      fullscreenClassName={fullscreenClassName}
      fullscreen_style={fullscreen_style}
      fullscreen={fullscreen}
      minHeight={width}
      minWidth={width}
      SpinnerDiv={SpinnerDiv}
      showSpinner={showSpinner}
    />
  );
};

Grid._dashprivate_isLoadingComponent = true;

Grid.defaultProps = {
  debounce: 0,
  show_initially: true,
  color: '#000000',
  speed_multiplier: 1,
  width: 57,
  margin: 2,
};

Grid.propTypes = {
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
   * The gap between the dots (in px)
   */
  margin: PropTypes.number,

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

export default Grid;
