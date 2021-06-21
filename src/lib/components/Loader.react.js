import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import {isNil} from 'ramda';
import {
    BarLoader,
    BeatLoader,
    BounceLoader,
    CircleLoader,
    ClimbingBoxLoader,
    ClipLoader,
    ClockLoader,
    DotLoader,
    FadeLoader,
    GridLoader,
    HashLoader,
    MoonLoader,
    PacmanLoader,
    PropagateLoader,
    PuffLoader,
    PulseLoader,
    RingLoader,
    RiseLoader,
    RotateLoader,
    ScaleLoader,
    SyncLoader,
} from 'react-spinners';

// Spinner options
function getSpinner(spinnerType) {
    switch (spinnerType) {
        case 'bar':
            return BarLoader;
        case 'beat':
            return BeatLoader;
        case 'bounce':
            return BounceLoader;
        case 'circle':
            return CircleLoader;
        case 'climbingBox':
            return ClimbingBoxLoader;
        case 'clip':
            return ClipLoader;
        case 'clock':
            return ClockLoader;
        case 'dot':
            return DotLoader;
        case 'fade':
            return FadeLoader;
        case 'grid':
            return GridLoader;
        case 'hash':
            return HashLoader;
        case 'moon':
            return MoonLoader;
        case 'pacman':
            return PacmanLoader;
        case 'propagate':
            return PropagateLoader;
        case 'puff':
            return PuffLoader;
        case 'pulse':
            return PulseLoader;
        case 'ring':
            return RingLoader;
        case 'rise':
            return RiseLoader;
        case 'rotate':
            return RotateLoader;
        case 'scale':
            return ScaleLoader;
        case 'sync':
            return SyncLoader;
        default:
            return ScaleLoader;
    }
}

const Loader = (props) => {
    const {
        children,
        color,
        type,
        loading_state,
        spinnerCSS,
        spinner_style,
        spinnerClassName,
        fullscreen,
        fullscreenClassName,
        fullscreen_style,
        debounce,
        show_initially,
        size,
        width,
        height,
        radius,
        margin,
        speedMultiplier,
        ...otherProps
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

    // Identify the spinner type
    const Spinner = getSpinner(type);

    // Get the spinner size
    var spinner_size = {};

    !isNil(radius) ? (spinner_size.radius = radius) : null;
    !isNil(margin) ? (spinner_size.margin = margin) : null;

    // This allows for a generic 'size' for all spinners
    if (type === 'bar') {
        !isNil(height)
            ? (spinner_size.height = height)
            : !isNil(size)
            ? (spinner_size.height = Math.ceil(size / 4))
            : null;
        !isNil(width)
            ? (spinner_size.width = width)
            : !isNil(size)
            ? (spinner_size.width = size)
            : null;
    } else if (type === 'fade') {
        !isNil(height)
            ? (spinner_size.height = height)
            : !isNil(size)
            ? (spinner_size.height = size)
            : null;
        !isNil(width)
            ? (spinner_size.width = width)
            : !isNil(size)
            ? (spinner_size.width = Math.ceil(size / 3))
            : null;
    } else if (type === 'scale') {
        !isNil(height)
            ? (spinner_size.height = height)
            : !isNil(size)
            ? (spinner_size.height = size)
            : null;
        !isNil(width)
            ? (spinner_size.width = width)
            : !isNil(size)
            ? (spinner_size.width = Math.ceil(size / 9))
            : null;
    } else {
        !isNil(size) ? (spinner_size.size = size) : null;
    }

    const SpinnerDiv = ({style}) => (
        <div
            className={spinnerClassName}
            style={{
                display: 'flex',
                width: '100%',
                height: '100%',
                justifyContent: 'center',
                alignItems: 'center',
                ...style,
            }}
        >
            <Spinner
                color={color}
                {...spinner_size}
                css={spinnerCSS}
                speedMultiplier={speedMultiplier}
            />
        </div>
    );

    // Fullscreen
    const fullscreenStyle = {
        position: 'fixed',
        width: '100vw',
        height: '100vh',
        top: 0,
        left: 0,
        backgroundColor: 'white',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 99,
        visibility: 'visible',
        ...fullscreen_style,
    };

    if (children) {
        const coveringStyle = {
            visibility: 'visible',
            position: 'absolute',
            top: 0,
            height: '100%',
            width: '100%',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
        };

        const hiddenStyle = {
            visibility: 'hidden',
            position: 'relative',
        };

        const spinnerStyle = {
            margin: '1rem auto',
            ...spinner_style,
        };

        return (
            <div style={showSpinner ? hiddenStyle : {}}>
                {children}
                {showSpinner && (
                    <div
                        style={fullscreen ? fullscreenStyle : coveringStyle}
                        className={fullscreen && fullscreenClassName}
                    >
                        <SpinnerDiv style={spinnerStyle} />
                    </div>
                )}
            </div>
        );
    }

    if (fullscreen) {
        return (
            <div className={fullscreenClassName} style={fullscreenStyle}>
                <SpinnerDiv style={spinner_style} />
            </div>
        );
    }

    return <SpinnerDiv style={spinner_style} />;
};

Loader._dashprivate_isLoadingComponent = true;

Loader.defaultProps = {
    debounce: 0,
    show_initially: true,
    color: '#000000',
    type: 'default',
    speedMultiplier: 1,
};

Loader.propTypes = {
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
     * Defines CSS styles for the container when fullscreen=True.
     */
    fullscreen_style: PropTypes.object,

    /**
     * Defines CSS styles for the container when fullscreen=False.
     */
    spinner_style: PropTypes.object,

    /**
     * Often used with CSS to style elements with common properties.
     */
    fullscreenClassName: PropTypes.string,

    /**
     * CSS class names to apply to the container when fullscreen=False.
     */
    spinnerClassName: PropTypes.string,

    /**
     * Sets the color of the Spinner. You can also specify any valid CSS color
     * of your choice (e.g. a hex code, a decimal code or a CSS color name).
     *
     * If not specified will default to black.
     */
    color: PropTypes.string,

    /**
     * Defines additional CSS styles for the spinner itself. It's based on the
     * emotion css styles here: https://emotion.sh/docs/introduction
     */
    spinnerCSS: PropTypes.object,

    /**
     * The type of spinner. Options are:
     * - bar
     * - beat
     * - bounce
     * - circle
     * - climbingBox
     * - clip
     * - clock
     * - dot
     * - fade
     * - grid
     * - hash
     * - moon
     * - pacman
     * - propagate
     * - puff
     * - pulse
     * - ring
     * - rise
     * - rotate
     * - scale
     * - sync
     */
    type: PropTypes.string,

    /**
     * The relative speed of the spinner
     */
    speedMultiplier: PropTypes.number,

    /**
     * The spinner size (in px) - not applicable for loaders of type:
     * - bar
     * - fade
     * - scale
     */
    size: PropTypes.number,

    /**
     * The spinner height (in px) - only applicable for loaders of type:
     * - bar
     * - fade
     * - scale
     */
    height: PropTypes.number,

    /**
     * The spinner width (in px) - only applicable for loaders of type:
     * - bar
     * - fade
     * - scale
     */
    width: PropTypes.number,

    /**
     * The spinner radius (in px) - only applicable for loaders of type:
     * - fade
     * - scale
     */
    radius: PropTypes.number,

    /**
     * The spinner margin (in px) - only applicable for loaders of type:
     * - beat
     * - dot
     * - fade
     * - hash
     * - moon
     * - pacman
     * - pulse
     * - ring
     * - rise
     * - rotate
     * - scale
     * - sync
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

export default Loader;
