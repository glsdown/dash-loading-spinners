import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
// import Loader from 'react-loader-spinner';
// import 'react-loader-spinner/dist/loader/css/react-spinner-loader.css';
import CoveringContainer from '../../private/CoveringContainer.react';

const ThreeDots = (props) => {
    const {
        children,
        color,
        secondaryColor,
        tertiaryColor,
        speedMultiplier,
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

    const SpinnerDiv = () => {
        const maxRadius = radius + 2 * Math.ceil(radius / 3);
        const animationTime = 0.8 / speedMultiplier;

        return (
            <svg
                width={width}
                height={height}
                viewBox={`0 0 ${width} ${height}`}
                xmlns="http://www.w3.org/2000/svg"
                aria-label="loading"
            >
                <circle cx="25%" cy="50%" r={maxRadius} fill={color}>
                    <animate
                        attributeName="r"
                        from={`${maxRadius}`}
                        to={`${maxRadius}`}
                        begin="0s"
                        dur={`${animationTime}s`}
                        values={`${maxRadius};${radius};${maxRadius}`}
                        calcMode="linear"
                        repeatCount="indefinite"
                    />
                    <animate
                        attributeName="fillOpacity"
                        from="1"
                        to="1"
                        begin="0s"
                        dur={`${animationTime}s`}
                        values="1;.25;1"
                        calcMode="linear"
                        repeatCount="indefinite"
                    />
                </circle>
                <circle
                    cx="50%"
                    cy="50%"
                    r={radius}
                    attributeName="fillOpacity"
                    from="1"
                    to="0.3"
                    fill={secondaryColor}
                >
                    <animate
                        attributeName="r"
                        from={`${radius}`}
                        to={`${radius}`}
                        begin="0s"
                        dur={`${animationTime}s`}
                        values={`${radius};${maxRadius};${radius}`}
                        calcMode="linear"
                        repeatCount="indefinite"
                    />
                    <animate
                        attributeName="fillOpacity"
                        from="0.25"
                        to="0.25"
                        begin="0s"
                        dur={`${animationTime}s`}
                        values=".25;1;.25"
                        calcMode="linear"
                        repeatCount="indefinite"
                    />
                </circle>
                <circle cx="75%" cy="50%" r={maxRadius} fill={tertiaryColor}>
                    <animate
                        attributeName="r"
                        from={`${maxRadius}`}
                        to={`${maxRadius}`}
                        begin="0s"
                        dur={`${animationTime}s`}
                        values={`${maxRadius};${radius};${maxRadius}`}
                        calcMode="linear"
                        repeatCount="indefinite"
                    />
                    <animate
                        attributeName="fillOpacity"
                        from="1"
                        to="1"
                        begin="0s"
                        dur={`${animationTime}s`}
                        values="1;.25;1"
                        calcMode="linear"
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
            minHeight={height}
            minWidth={width}
            SpinnerDiv={SpinnerDiv}
            showSpinner={showSpinner}
        />
    );
};

ThreeDots._dashprivate_isLoadingComponent = true;

ThreeDots.defaultProps = {
    debounce: 0,
    show_initially: true,
    speedMultiplier: 1,
    color: '#000000',
    secondaryColor: '#0275d8',
    tertiaryColor: '#5cb85c',
    width: 120,
    height: 30,
    radius: 6,
};

ThreeDots.propTypes = {
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
     * Sets the color of the Spinner. You can also specify any valid CSS color
     * of your choice (e.g. a hex code, a decimal code or a CSS color name).
     *
     * If not specified will default to green.
     */
    tertiaryColor: PropTypes.string,

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

export default ThreeDots;
