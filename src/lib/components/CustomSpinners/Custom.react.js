import React, {useEffect, useRef, useState} from 'react';
import PropTypes from 'prop-types';
import CoveringContainer from '../../private/CoveringContainer.react';

const Spinner = ({svg, visible}) => {
    if (!visible || visible === 'false') {
        return null;
    }
    return <div dangerouslySetInnerHTML={{__html: svg}} />;
};

const Custom = (props) => {
    const {
        children,
        loading_state,
        fullscreenClassName,
        fullscreen_style,
        fullscreen,
        debounce,
        show_initially,
        svg,
        width,
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

    const SpinnerDiv = () => <Spinner visible={loading_state} svg={svg} />;

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

Custom._dashprivate_isLoadingComponent = true;

Custom.defaultProps = {
    debounce: 0,
    show_initially: true,
    width: 80,
    svg: `<svg
    width=80
    height=80
    viewBox="0 0 38 38"
    xmlns="http://www.w3.org/2000/svg"
    aria-label="Loading"
  >
    <defs>
      <linearGradient x1="8.042%" y1="0%" x2="65.682%" y2="23.865%" id="a">
        <stop stopColor="black" stopOpacity="0" offset="0%" />
        <stop stopColor="black" stopOpacity=".631" offset="63.146%" />
        <stop stopColor="black" offset="100%" />
      </linearGradient>
    </defs>
    <g fill="none" fillRule="evenodd">
      <g transform="translate(1 1)">
        <path d="M36 18c0-9.94-8.06-18-18-18" id="Oval-2" stroke="black" strokeWidth="2">
          <animateTransform
            attributeName="transform"
            type="rotate"
            from="0 18 18"
            to="360 18 18"
            dur="0.9s"
            repeatCount="indefinite"
          />
        </path>
        <circle fill="#fff" cx="36" cy="18" r=1>
          <animateTransform
            attributeName="transform"
            type="rotate"
            from="0 18 18"
            to="360 18 18"
            dur="0.9s"
            repeatCount="indefinite"
          />
        </circle>
      </g>
    </g>
  </svg>`,
};

Custom.propTypes = {
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
     * The SVG code to include as the spinner
     */
    svg: PropTypes.string,

    /**
     * The width of the resultant SVG (in px)
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

export default Custom;
