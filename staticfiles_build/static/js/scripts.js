notification = {
    primary: function (message, from, align) {
        const notyf = new Notyf({
            position: {
                x: align, // left or right
                y: from, // bottom or top
            },
            types: [
                {
                    type: 'info',
                    background: '#262B40',
                    icon: {
                        className: 'fas fa-comment-dots',
                        tagName: 'span',
                        color: '#fff'
                    },
                    dismissible: false,
                    speed: 9000
                }
            ]
        });
        notyf.open({
            type: 'info',
            message: message
        });
    },
    info: function (message, from, align) {
        const notyf = new Notyf({
            position: {
                x: align, // left or right
                y: from, // bottom or top
            },
            types: [
                {
                    type: 'info',
                    background: '#0948B3',
                    icon: {
                        className: 'fas fa-comment-dots',
                        tagName: 'span',
                        color: '#fff'
                    },
                    dismissible: false
                }
            ]
        });
        notyf.open({
            type: 'info',
            message: message
        });
    },
    success: function (message, from, align) {
        const notyf = new Notyf({
            position: {
                x: align, // left or right
                y: from, // bottom or top
            },
            types: [
                {
                    type: 'info',
                    background: '#92f16d',
                    icon: {
                        className: 'fas fa-comment-dots',
                        tagName: 'span',
                        color: '#fff'
                    },
                    dismissible: false
                }
            ]
        });
        notyf.open({
            type: 'info',
            message: message
        });
    },
    warning: function (message, from, align) {
        const notyf = new Notyf({
            position: {
                x: align, // left or right
                y: from, // bottom or top
            },
            types: [
                {
                    type: 'warning',
                    background: '#F5B759',
                    icon: {
                        className: 'fas fa-comment-dots',
                        tagName: 'span',
                        color: '#fff'
                    },
                    dismissible: false
                }
            ],
            delay: 9000
        });
        notyf.open({
            type: 'warning',
            message: message
        });
    },
    danger: function (message, from, align) {
        const notyf = new Notyf({
            position: {
                x: align, // left or right
                y: from, // bottom or top
            },
            types: [
                {
                    type: 'error',
                    background: '#FA5252',
                    icon: {
                        className: 'fas fa-comment-dots',
                        tagName: 'span',
                        color: '#fff'
                    },
                    dismissible: false
                }
            ]
        });
        notyf.open({
            type: 'error',
            message: message
        });
    }
};

const checkboxs = document.querySelectorAll('input[type=checkbox]');
for (var i = 0; i < checkboxs.length; i++) {
    checkboxs[i].classList.add('form-check-input');
}

const texts = document.querySelectorAll('select');
for (var y = 0; y < texts.length; y++) {
    texts[y].classList.add('form-select');
}

const r = document.querySelectorAll('input[type=text], input[type=email], input[type=password], input[type=number], textarea');
for (var z = 0; z < r.length; z++) {
    r[z].classList.add('form-control');
}
