document.body.innerHTML +=

    '<div id="left_panel" class="navigation">' +

    '<a href="/"><img src="/logo.png" alt="Sewosy" /></a>' +

    '<a href="/About_Us">About Us</a>' +

    '<a href="/Contact_Us">Contact Us</a>' +

    '</div>'

const menu = new URLSearchParams(window.location.search).get('menu')

if (menu == null) {

    fetch('/home')

        .then(

            function (response) {

                if (response.status !== 200) {

                    console.log(response.status)

                    return;
                }

                response.json().then(function (arr) {

                    var right_panel =

                        '<div id="right_panel" class="navigation">' +

                        '<a href="#" id="arrows">' +

                        '<i onclick="change_arrows_and_menu_items(1)" class="fa-solid fa-circle-arrow-right"></i>' +

                        '</a>'

                    var list = ''

                    for (var i = 0; i < arr.length; i++) {

                        list += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '">' + arr[i].pages + '</a>'
                    }

                    document.body.innerHTML += right_panel + list + '</div>'
                });
            }
        )
        .catch(function (err) {

            alert(err)
        });
}


if (menu == 1) {

    fetch('/menu_1')

        .then(

            function (response) {

                if (response.status !== 200) {

                    alert(response.status)

                    return
                }

                response.json().then(function (arr) {

                    var right_panel =

                        '<div id="right_panel" class="navigation">' +

                        '<a href="#" id="arrows">' +

                        '<i onclick="change_arrows_and_menu_items(0)" class="fa-solid fa-circle-arrow-left"></i>' +

                        '&nbsp&nbsp&nbsp&nbsp' +

                        '<i onclick="change_arrows_and_menu_items(2)" class="fa-solid fa-circle-arrow-right"></i>' +

                        '</a>'

                    var list = ''

                    for (var i = 0; i < arr.length; i++) {

                        list += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '?menu=1">' + arr[i].pages + '</a>';
                    }

                    document.body.innerHTML += right_panel + list + '</div>'
                });
            }
        )
        .catch(function (err) {

            alert('Fetch Error :-S ' + err)
        });
}

if (menu == 2) {

    fetch('/menu_2')

        .then(

            function (response) {

                if (response.status !== 200) {

                    console.log(response.status)

                    return;
                }

                var right_panel =

                    '<div id="right_panel" class="navigation">' +

                    '<a href="#" id="arrows">' +

                    '<i onclick="change_arrows_and_menu_items(3)" class="fa-solid fa-circle-arrow-left"></i>' +

                    '</a>'

                var list = ''

                response.json().then(function (arr) {

                    for (var i = 0; i < arr.length; i++) {

                        list += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '?menu=2">' + arr[i].pages + '</a>';
                    }

                    document.body.innerHTML += right_panel + list + '</div>'
                });
            }
        )
        .catch(function (err) {

            alert('Fetch Error :-S ' + err)
        });
}

fetch('/top_menu')

    .then(

        function (response) {

            if (response.status !== 200) {

                alert('Status Code: ' + response.status)

                return;
            }

            response.json().then(function (arr) {

                var top_navigation =

                    '<div class="top_navigation">' +

                    '<a href="javascript:void(0);" class="icon" id="icon">' +

                    '<i class="fa fa-bars" onclick="toggle_menu(true)"></i>' +

                    '</a>' +

                    '<a href="/">' +

                    '<img src="/logo.png" alt="Sewosy" />' +

                    '</a>' +

                    '</div>' +

                    '<div id="menu" class="navigation" hidden>'

                var list = ''

                for (var i = 0; i < arr.length; i++) {

                    if (arr[i].pages == "Installation Video") {

                        list += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '">Aluminium Door Handle Installation Video</a>'

                    } else if (arr[i].pages == "Extensions") {

                        list += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '">Aluminium Door Handle Extensions</a>'

                    } else {

                        list +=

                            '<a href="/' + arr[i].pages.replace(/ /g, "_") + '">' + arr[i].pages + '</a>'
                    }
                }

                document.body.innerHTML += top_navigation + list + '<br/><br/><br/></div>'
            });
        }
    )
    .catch(function (err) {

        alert('Fetch Error :-S ' + err)
    });

function change_arrows_and_menu_items(value) {

    document.getElementById("right_panel").innerHTML = ''

    var append = '<a href="#" id="arrows">'

    if (value == 0) {

        append += '<i onclick="change_arrows_and_menu_items(1)" class="fa-solid fa-circle-arrow-right"></i>'

        fetch('/home')
            .then(
                function (response) {

                    if (response.status !== 200) {
                        document.getElementById('right_panel').innerHTML = 'Looks like there was a problem. Status Code: ' + response.status
                        return;
                    }

                    response.json().then(function (arr) {

                        for (var i = 0; i < arr.length; i++) {

                            append += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '">' + arr[i].pages + '</a>';

                        }

                        document.getElementById("right_panel").innerHTML = append
                    });
                }
            )
            .catch(function (err) {
                document.getElementById("right_panel").innerHTML = 'Fetch Error :-S ' + err
            });
    }

    if (value == 1) {

        append += '<i onclick="change_arrows_and_menu_items(0)" class="fa-solid fa-circle-arrow-left"></i>' +
            '&nbsp&nbsp&nbsp&nbsp' +
            '<i onclick="change_arrows_and_menu_items(2)" class="fa-solid fa-circle-arrow-right"></i>' +
            '</a>'

        fetch('/menu_1')
            .then(
                function (response) {

                    if (response.status !== 200) {
                        document.getElementById('right_panel').innerHTML = 'Looks like there was a problem. Status Code: ' + response.status
                        return;
                    }

                    response.json().then(function (arr) {

                        for (var i = 0; i < arr.length; i++) {

                            append += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '?menu=1">' + arr[i].pages + '</a>';

                        }

                        document.getElementById("right_panel").innerHTML = append
                    });
                }
            )
            .catch(function (err) {
                document.getElementById("right_panel").innerHTML = 'Fetch Error :-S ' + err
            });

    }

    if (value == 2) {

        append += '<i onclick="change_arrows_and_menu_items(3)" class="fa-solid fa-circle-arrow-left"></i>' +
            '</a>'

        fetch('/menu_2')
            .then(
                function (response) {

                    if (response.status !== 200) {
                        document.getElementById('right_panel').innerHTML = 'Looks like there was a problem. Status Code: ' + response.status
                        return;
                    }

                    response.json().then(function (arr) {

                        for (var i = 0; i < arr.length; i++) {

                            append += '<a href="/' + arr[i].pages.replace(/ /g, "_") + '?menu=2">' + arr[i].pages + '</a>';

                        }

                        document.getElementById("right_panel").innerHTML = append
                    });
                }
            )
            .catch(function (err) {
                document.getElementById("right_panel").innerHTML = 'Fetch Error :-S ' + err
            });
    }

    if (value == 3) {

        change_arrows_and_menu_items(1)
    }
}

function change_content(element, number, overview_or_spec) {

    element.style.background = "slategray"
    element.style.color = "white"
    element.style.textShadow = "1px 1px black"

    document.getElementById(overview_or_spec + number).style.color = "black";
    document.getElementById(overview_or_spec + number).style.background = "white";
    document.getElementById(overview_or_spec + number).style.textShadow = "none";

    if (overview_or_spec == "overview_") {
        document.getElementById("overview_content_" + number).setAttribute("hidden", true);
        document.getElementById("overview_spec_" + number).removeAttribute("hidden");
    }
    else {
        document.getElementById("overview_content_" + number).removeAttribute("hidden");
        document.getElementById("overview_spec_" + number).setAttribute("hidden", true);
    }

}

function toggle_menu(value) {

    if (value) {

        document.getElementById("menu").removeAttribute("hidden");

        document.getElementById("icon").innerHTML = '<i class="fa fa-bars" onclick="toggle_menu(false)"></i>'

        document.getElementById("icon").style.color = "cyan"

        document.body.style.overflow = "hidden"
    }
    else {

        document.getElementById("menu").setAttribute("hidden", true);

        document.getElementById("icon").innerHTML = '<i class="fa fa-bars" onclick="toggle_menu(true)"></i>'

        document.getElementById("icon").style.color = "black"

        document.body.style.overflow = "auto"
    }


}


