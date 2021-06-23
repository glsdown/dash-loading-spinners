import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import Loader from 'react-loader-spinner';
import 'react-loader-spinner/dist/loader/css/react-spinner-loader.css';
import CoveringContainer from '../../private/CoveringContainer.react';

const Rings = (props) => {
    const {
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
                timer.current = setTimeout(
                    () => setShowSpinner(false),
                    debounce
                );
            }
        }
    }, [loading_state]);

    const SpinnerDiv = () => (
        <Loader
            type="Rings"
            visible={loading_state}
            color={color}
            height={height}
            width={width}
            radius={radius}
        />
    );

    return (
        <CoveringContainer
            children={children}
            fullscreen={fullscreen}
            fullscreenClassName={fullscreenClassName}
            fullscreen_style={fullscreen_style}
            minWidth={width}
            SpinnerDiv={SpinnerDiv}
            showSpinner={showSpinner}
        />
    );
};

Rings._dashprivate_isLoadingComponent = true;

Rings.defaultProps = {
    debounce: 0,
    show_initially: true,
    color: '#000000',
    width: 80,
    height: 80,
};

Rings.propTypes = {
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
     * The relative speed of the spinner
     */
    speedMultiplier: PropTypes.number,

    /**
     * The spinner height (in px)
     */
    height: PropTypes.number,

    /**
     * The spinner width (in px)
     */
    width: PropTypes.number,

    /**
     * The spinner radius (in px)
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

export default Rings;
