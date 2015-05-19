//blog angular
var HOST = 'http://localhost:8000';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var blogApp = angular.module("blogApp", []);
blogApp.filter('trustHtml', function ($sce) {
    return function (input) {
        return $sce.trustAsHtml(input);
    }
});

//index
blogApp.controller("indexController", function ($scope, $http, $window) {
    var url = HOST + '/index_content/';
    $http.get(url).success(function (response) {
        $scope.blog = response.body.blog;
        $scope.pagination = response.body.pagination;
    });
});

//blog_list
blogApp.controller("blogController", function ($scope, $http, $window) {
    $scope.req_type = function () {
        var req_url = window.location.href.toString();
        var url_para = req_url.split('/');
        var url = '';
        if (url_para[3] == 'classify') {
            url = HOST + "/get_classify/" + url_para[4] + "/";
        } else if (url_para[3] == 'tag') {
            url = HOST + "/get_tag/" + url_para[4] + "/";
        } else {
            url = HOST + "/bd/";
        }
        return url;
    };
    $scope.req_http = function (para) {
        if (para == 0) {
            alert("木有啦");
            return null;
        }
        var url = $scope.req_type() + '?page=' + para;
        $http.get(url).success(function (response) {
            $scope.blogs = response.body.blog_list;
            $scope.pagination = response.body.pagination;
        });
    };
    var url = $scope.req_type();
    $http.get(url).success(function (response) {
        $scope.blogs = response.body.blog_list;
        $scope.pagination = response.body.pagination;
    });
});

//base tools
blogApp.controller("toolController", function ($scope, $http) {
    url = HOST + "/tools/";
    $http.get(url).success(function (res) {
        $scope.latest_list = res.body.latest_list;
        $scope.classifies = res.body.classify_list;
        $scope.read_list = res.body.read_list;
    });
});

//blog detail
blogApp.controller("blogDetailController", function ($scope, $http, $window) {
    $scope.verifyp = '';
    $scope.is_reply = false;
    $scope.to_the = '';
    $scope.masterId = '';
    $scope.toId = '';
    var req_url = window.location.href.toString();
    var url_para = req_url.split('/')[4];
    $scope.req_http = function (url) {
        url = HOST + '/blog/' + url + "/";
        $http.get(url).success(function (response) {
            $scope.blog = response.body.blog;
            $scope.pagination = response.body.pagination;
            $scope.comment = response.body.comment;
            $scope.have_comment = response.body.have_comment;
        });
    };
    $scope.cancel_reply = function () {
        $scope.is_reply = false;
        $scope.masterId = '';
        $scope.to_the = '';
        $scope.toId = '';
    };
    $scope.reply = function (to, mid, tid) {
        $scope.masterId = mid;
        $scope.toId = tid;
        $scope.to_the = to;
        $scope.is_reply = true;
    };
    $scope.sub_reply = function (to, mid, tid) {
        $scope.masterId = mid;
        $scope.toId = tid;
        $scope.to_the = to;
        $scope.is_reply = true;
    };
    $scope.submit_comment = function () {
        url = window.location.href.toString();
        +"comment/"
        $http.get(url).success(function (response) {
            $scope.blog = response.body.blog;
            $scope.pagination = response.body.pagination;
            $scope.comment = response.body.comment;
            $scope.have_comment = response.body.have_comment;
        });
    };
    var url = HOST + "/detail/" + url_para + '/';
    $http.get(url).success(function (response) {
        //toolApp.$scope.req_http();
        $scope.blog = response.body.blog;
        $scope.pagination = response.body.pagination;
        $scope.comments = response.body.comment;
        $scope.have_comment = response.body.have_comment;
        $scope.verifyp = response.body.verify;
    });
    $scope.refresh_req = function (url) {
        url = HOST + "/refresh_verify/";
        $http.get(url).success(function (response) {
            $scope.verifyp = response.body.verify;
        });
    };
    $scope.commentData = {'verify': '', 'content': ''};
    $scope.verify = false;
    $scope.content = false;
    req_url = window.location.href.toString();
    $scope.bid = req_url.split('/')[4];
    $scope.verifyChange = function () {
        $scope.verify = false;
    };
    $scope.contentChange = function () {
        $scope.content = false;
    };
    $scope.processForm = function () {
        if ($scope.commentData.verify == '') {
            $scope.verify = true;
            if ($scope.commentData.content == '') {
                $scope.content = true;
            }
            return null;
        }
        if ($scope.commentData.content == '') {
            $scope.content = true;
            return null;
        }
        if ($scope.is_reply){
            $scope.commentData.mid = $scope.masterId;
            $scope.commentData.tid = $scope.toId;
            $scope.commentData.to = $scope.to_the;
        }
        $http({
            method: 'POST',
            url: HOST + '/blog/comment/' + $scope.bid + '/',
            data: $.param($scope.commentData),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function (data) {
                if (data.status == 1) {
                    $window.location.reload();
                } else {
                    var error_mes = data.body.fail_mes;
                    alert(error_mes);
                }
            });
    };
});


//konwledge
blogApp.controller("knowController", function ($scope, $http) {
    $scope.search_text = '';
    $scope.req_http = function (url) {
        if (url == 0) {
            alert("木有啦");
            return null;
        }
        if ($scope.search_text == '') {
            url = HOST + '/get_knowledge?page=' + url;
        } else {
            url = HOST + '/get_knowledge/' + $scope.search_text + '/?page=' + url;
        }
        $http.get(url).success(function (response) {
            $scope.knowledges = response.body.know_list;
            $scope.pagination = response.body.pagination;
        });
    };
    $scope.search_http = function () {
        if ($scope.search_text == '') {
            url = HOST + '/get_knowledge/';
        } else {
            url = HOST + '/get_knowledge/' + $scope.search_text + '/';

        }
        $http.get(url).success(function (response) {
            $scope.knowledges = response.body.know_list;
            $scope.pagination = response.body.pagination;
        });
    };
    var url = HOST + "/get_knowledge/";
    $http.get(url).success(function (response) {
        //toolApp.$scope.req_http();
        $scope.knowledges = response.body.know_list;
        $scope.pagination = response.body.pagination;
    });
});
//ng-cloak class="ng-cloak" ng-app="toolApp" ng-controller="toolController"

//lab
blogApp.controller("labController", function ($scope, $http) {
     var url = HOST + "/lab/get_lab_info/";
    $scope.api_status = false;
    $http.get(url).success(function (response) {
        //toolApp.$scope.req_http();
        $scope.total_user = response.body.total_user;
        $scope.req_times = response.body.req_times;
        $scope.proxy_num = response.body.proxy_num;
        $scope.update_time = response.body.update_time;
        $scope.api_control = response.body.api_control;
        $scope.api_status = response.body.api_status;
    });
});

//lab_proxy
blogApp.controller("labProxyController", function ($scope, $http) {
    $scope.proxyData = {'private_token': 'rapospectre', 'reset': true};
    $scope.token = '';
    $scope.processToken = function () {
        var url = HOST + "/lab/create_token/";
        $http.get(url).success(function (response) {
            $scope.token = response.body.private_token;
        });
    };
    $http({
            method: 'POST',
            url: HOST + "/lab/get_proxy/",
            data: $.param($scope.proxyData),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function (data) {
                if (data.status == 1) {
                    $scope.proxy_list = data.body.proxy_list
                }
            });
});


//lab_monitor



//admin
var adminApp = angular.module("adminApp", []);
adminApp.controller("articleController", function ($scope, $http, $window) {
    $scope.blogData = {'caption': '', 'content': '', 'sub_caption': '', 'classify': '', 'publish': false, 'tags': ''};
    $scope.mutags = null;
    $scope.newTag = '';
    $scope.newClassify = '';
    req_url = window.location.href.toString();
    ex_para = req_url.split('/');
    $scope.processForm = function () {
        if ($scope.blogData.caption == '') {
            return null;
        }
        var tags = '';
        for (var itm in $scope.blogData.tags) {
            tags = tags + $scope.blogData.tags[itm].id + ','
        }
        $scope.blogData.id = ex_para[5];
        $scope.blogData.tags = tags;
        $http({
            method: 'POST',
            url: HOST + '/blog_admin/new_blog/',
            data: $.param($scope.blogData),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function (data) {
                console.log(data);
                if (data.status == 1) {
                    // if not successful, bind errors to error variables
                    alert('发布成功！');
                    //$window.location.reload();
                    //$scope.errorSuperhero = data.errors.superheroAlias;
                } else {
                    // if successful, bind success message to message
                    var error_mes = data.body.fail_mes;
                    alert(error_mes);
                }
            });
    };
    $scope.newReq = function (type) {
        var para = null;
        var url = '';
        if (type == 1) {
            para = {'classify': $scope.newClassify};
            url = HOST + '/blog_admin/new_classify/';
        } else {
            para = {'tag': $scope.newTag};
            url = HOST + '/blog_admin/new_tag/';
        }
        $http({
            method: 'POST',
            url: url,
            data: $.param(para),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function (data) {
                console.log(data);
                if (data.status == 1) {
                    // if not successful, bind errors to error variables
                    alert('增加成功！');
                    if (data.body.type == 1) {
                        $scope.classifies = data.body.classify;
                    } else {
                        $scope.tags = data.body.tags;
                    }
                } else {
                    // if successful, bind success message to message
                    var error_mes = data.body.fail_mes;
                    alert(error_mes);
                }
            });
    };
    var url = HOST + "/blog_admin/blog_util/";
    req_url = window.location.href.toString();
    paras = req_url.split('/');
    if (paras[5] != '') {
        url = url + paras[5] + '/';
    }
    $http.get(url).success(function (response) {
        if (response.status == 1) {
            $scope.tags = response.body.tags;
            $scope.classifies = response.body.classify;
            if (paras[5] != '') {
                $scope.blogData.caption = response.body.blog.caption;
                $scope.blogData.sub_caption = response.body.blog.sub_caption;
                $scope.blogData.content = response.body.blog.content;
                $scope.blogData.classify = response.body.blog.classification;
                $scope.blogData.tags = response.body.blog.tags;
                $scope.blogData.publish = response.body.blog.publish;
            }
        } else if (response.status == 9) {
            $window.location.href = "/blog_admin/";
        }
    });
});

//knowadmin
adminApp.controller("knowAdminController", function ($scope, $http, $window) {
    $scope.knowData = {'id': '', 'question': '', 'answer': '', 'env': '', 'publish': false};
    $scope.newEnv = '';
    $scope.knowForm = function () {
        var tmp_str = '';
        for (var itm in $scope.knowData.env) {
            tmp_str = tmp_str + $scope.knowData.env[itm].id + ',';
        }
        $scope.knowData.env = tmp_str;
        $http({
            method: 'POST',
            url: HOST + '/blog_admin/new_know/',
            data: $.param($scope.knowData),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function (data) {
                if (data.status == 1) {
                    // if not successful, bind errors to error variables
                    alert('增长姿势成功！');
                    //$window.location.reload();
                } else {
                    // if successful, bind success message to message
                    var error_mes = data.body.fail_mes;
                    alert(error_mes);
                }
            });
    };
    $scope.newReq = function () {
        para = {'env': $scope.newEnv};
        $http({
            method: 'POST',
            url: HOST + "/blog_admin/new_env/",
            data: $.param(para),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        })
            .success(function (data) {
                if (data.status == 1) {
                    // if not successful, bind errors to error variables
                    alert('增加env成功！');
                    $scope.envs = data.body.env;
                    //$window.location.reload();
                } else {
                    // if successful, bind success message to message
                    var error_mes = data.body.fail_mes;
                    alert(error_mes);
                }
            });
    };
    var url = HOST + "/blog_admin/get_env/";
    req_url = window.location.href.toString();
    paras = req_url.split('/');
    //alert(para[5]);
    if (paras[5] != '') {
        url = url + paras[5] + '/';
    }
    $http.get(url).success(function (response) {
        if (response.status == 1) {
            $scope.envs = response.body.env;
            if (paras[5] != '') {
                $scope.knowData = response.body.know;
            }
        } else if (response.status == 9) {
            $window.location.href = "/blog_admin/";
        }
    });
});

//blog_list_admin
adminApp.controller("blogListAdminController", function ($scope, $http, $window) {
    $scope.opt = false;
    var url = HOST + '/blog_admin/blog_list/';
    $http.get(url).success(function (response) {
        if (response.status == 1) {
            $scope.blog_list = response.body.blog_list;
        } else if (response.status == 9) {
            $window.location.href = "/blog_admin/";
        }
    });
    $scope.blogOpt = function (type, bid) {
        para = {"type": type, "bid": bid};
        $http({
            method: 'POST',
            url: HOST + "/blog_admin/blog_opt/",
            data: $.param(para),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        }).success(function (data) {
            if (data.status == 1) {
                // if not successful, bind errors to error variables
                //alert('操作成功！');
                $scope.opt = true;
                $window.location.reload();
            } else {
                console.log(data);
                alert('操作失败');
            }
        }).fail(function (data) {
            //alert(data);
        });
    };
});

//comment_admin
adminApp.controller("commentListAdminController", function ($scope, $http, $window) {
    $scope.newR = '';
    var url = HOST + '/blog_admin/comment_list/';
    $http.get(url).success(function (response) {
        if (response.status == 1) {
            $scope.comment_list = response.body.comment_list;
        } else if (response.status == 9) {
            $window.location.href = "/blog_admin/";
        }
    });
    $scope.commentOptDel = function (type, cid) {
        para = {"type": type, "cid": cid};
        $http({
            method: 'POST',
            url: HOST + "/blog_admin/comment_opt_del/",
            data: $.param(para),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        }).success(function (data) {
            console.log(data);
            if (data.status == 1) {
                // if not successful, bind errors to error variables
                $window.location.reload();
            } else {
                console.log(data);
                alert('操作失败');
            }
        }).fail(function (data) {
            //alert(data);
        });
    };
    $scope.commentOptNew = function (type, cid, to) {
        para = {"type": type, "cid": cid, "to": to, "content": ''};
        var inputId = '';
        if (type == 1) {
            inputId = 'reply' + cid;
        } else {
            inputId = 'replys' + to;
        }
        var con = document.getElementById(inputId).value;
        para.content = con;
        $http({
            method: 'POST',
            url: HOST + "/blog_admin/comment_opt_new/",
            data: $.param(para),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        }).success(function (data) {
            console.log(data);
            if (data.status == 1) {
                $window.location.reload();
            } else {
                console.log(data);
                //alert('操作失败');
            }
        }).fail(function (data) {
            //alert(data);
        });
    };
});

//know_list_admin
adminApp.controller("knowListAdminController", function ($scope, $http, $window) {
    var url = HOST + '/blog_admin/know_list/';
    $http.get(url).success(function (response) {
        if (response.status == 1) {
            $scope.know_list = response.body.know_list;
        } else if (response.status == 9) {
            $window.location.href = "/blog_admin/";
        }
    });
    $scope.blogOpt = function (type, kid) {
        para = {"type": type, "kid": kid};
        $http({
            method: 'POST',
            url: HOST + "/blog_admin/know_opt/",
            data: $.param(para),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        }).success(function (data) {
            console.log(data);
            if (data.status == 1) {
                // if not successful, bind errors to error variables
                //alert('操作成功！');
                $window.location.reload();
            } else {
                console.log(data);
                alert('操作失败');
            }
        }).fail(function (data) {
            //alert(data);
        });
    };
});

//login_admin
adminApp.controller("loginAdminController", function ($scope, $http, $window) {
    $scope.accountData = {'account': '', 'password': '', 'csrfmiddlewaretoken': ''};
    $scope.haveError = false;
    $scope.errMes = '';
    $scope.mesChange = function () {
        $scope.haveError = false;
        $scope.errMes = '';
    };
    $scope.loginOpt = function () {
        var csrf = getCookie('csrftoken');
        $scope.accountData.csrfmiddlewaretoken = csrf;
        $http({
            method: 'POST',
            url: HOST + "/blog_admin/login/",
            data: $.param($scope.accountData),  // pass in data as strings
            headers: {'Content-Type': 'application/x-www-form-urlencoded'}  // set the headers so angular passing info as form data (not request payload)
        }).success(function (data) {
            if (data.status == 1) {
                $window.location.href = "/blog_admin/blog_admin/";
            } else {
                $scope.errMes = data.body.fail_mes;
                $scope.haveError = true;
            }
        });
    };
});