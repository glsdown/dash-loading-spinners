import React from 'react';

const CoveringContainer = (props) => {
    const {
        children,
        fullscreenClassName,
        fullscreen_style,
        fullscreen,
        minWidth,
        SpinnerDiv,
        showSpinner,
    } = props;

    // Required style
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

    const coveringStyle = {
        visibility: 'visible',
        position: 'absolute',
        top: 0,
        height: '100%',
        minWidth: minWidth,
        width: '100%',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '1rem auto',
    };

    const hiddenStyle = {
        visibility: 'hidden',
        position: 'relative',
    };

    return (
        <div style={showSpinner ? hiddenStyle : {}}>
            {children}
            {showSpinner && (
                <div
                    style={fullscreen ? fullscreenStyle : coveringStyle}
                    className={fullscreen ? fullscreenClassName : null}
                >
                    <SpinnerDiv />
                </div>
            )}
        </div>
    );
};

export default CoveringContainer;
