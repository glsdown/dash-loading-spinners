import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import {Ellipsis as EllipsisSpinner} from 'react-css-spinners';
import CoveringContainer from '../../private/CoveringContainer.react';

const Ellipsis = (props) => {
    const {
        children,
        color,
        loading_state,
        fullscreenClassName,
        fullscreen_style,
        fullscreen,
        debounce,
        show_initially,
        size,
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

    const SpinnerDiv = () => <EllipsisSpinner color={color} size={size} />;

    return (
        <CoveringContainer
            children={children}
            fullscreen={fullscreen}
            fullscreenClassName={fullscreenClassName}
            fullscreen_style={fullscreen_style}
            minHeight={size}
            minWidth={size}
            SpinnerDiv={SpinnerDiv}
            showSpinner={showSpinner}
        />
    );
};

Ellipsis._dashprivate_isLoadingComponent = true;

Ellipsis.defaultProps = {
    debounce: 0,
    show_initially: true,
    color: '#000000',
    size: 60,
};

Ellipsis.propTypes = {
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
     * The spinner size
     */
    size: PropTypes.number,

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

export default Ellipsis;
