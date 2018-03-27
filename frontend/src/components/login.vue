<template>
  <div class="popbox">
    <div id="J_popmask" class="popmask fadeIn animated"></div>
    <div class="loginbox">
      <a href="javascript:;" class="popbox-close">×</a>
      <div class="login login-modern" id="J-login">
      <form name="loginForm" id="login" action="https://authet15.alipay.com:443/login/homeB.htm" method="post"
            class="ui-form" novalidate="novalidate" data-widget-cid="widget-3" data-qrcode="false">
        <fieldset>
          <h2 class="ui-form-title " id="J-login-title">登录支付宝</h2>
          <div class="sl-error" id="J-errorBox" errortype="">
            <span class="sl-error-text"></span>
          </div>

          <div class="ui-form-item" id="J-username">
            <label id="J-label-user" class="ui-label">
              <span class="ui-icon ui-icon-userDEF"><i class="iconfont icon-yonghu"></i></span>
            </label>
            <!-- FD:130:authcenter/login/accountPlaceholder.vm:START -->
            <!-- FD:130:authcenter/login/accountPlaceholder.vm:END -->
            <input type="text" id="J-input-user" class="ui-input ui-input-normal" name="logonId" value="" autocomplete="off" maxlength="100" placeholder="邮箱/手机号/淘宝会员名"">
            <span class="sl-delect" seed="authcenter-account-delete"><i class="iconfont" title="删除"></i></span>
            <div class="ui-form-explain"></div>
          </div>

          <div class="ui-form-item ui-form-item-20pd" id="J-password">
            <label id="J-label-editer" class="ui-label" data-desc="登录密码" seed="authcenter-switch-aliedit">
              <span class="ui-icon ui-icon-securityON" id="safeSignCheck"><i class="iconfont icon-password"></i></span>
              <div id="J-label-editer-pop" class="ui-poptip fn-hide" data-widget-cid="widget-0">
                <div class="ui-poptip-container">
                  <div class="ui-poptip-arrow ui-poptip-arrow-7">
                    <em></em>
                    <span></span>
                  </div>
                  <div data-role="content" class="ui-poptip-content">点此选择密码控件登录</div>
                </div>
              </div>
            </label>

            <input style="display:none" seed="JPassword-ipt" smartracker="on">
            <input type="password" style="display:none" seed="JPassword-iptT1" smartracker="on">

            <span class="standardPwdContainer" style="display:none">
              <input type="password" id="password_input" name="password_input" class="ui-input" oncontextmenu="return false" onpaste="return false" oncopy="return false" oncut="return false" autocomplete="off">
            </span>
            <span class="alieditContainer" id="password_container">
              <input type="password" id="password_rsainput" name="password_rsainput" class="ui-input i-text" oncontextmenu="return false" onpaste="return false" oncopy="return false" oncut="return false" autocomplete="off" value="">
            </span>

            <p class="ui-form-other ui-form-other-fg">
              <a class="textlink forgot" href="https://accounts.alipay.com/console/dispatch.htm?scene_code=resetQueryPwd&amp;page_type=fullpage&amp;site=1" target="_blank">忘记登录密码？</a>
            </p>
            <div class="ui-form-explain"></div>
          </div>

          <div id="J-checkcode" class="ui-form-item fn-hide">
            <label id="J-label-checkcode" class="ui-label">
              <i class="ui-icon iconauth ui-icon-checkcodeT" id="J-switchCheckcode"></i>
              <div id="J-label-checkcode-pop" class="ui-poptip fn-hide">
                <div class="ui-poptip-container">
                  <div class="ui-poptip-arrow ui-poptip-arrow-7">
                    <em></em>
                    <span></span>
                  </div>
                  <div data-role="content" class="ui-poptip-content">点此选择语音校验码</div>
                </div>
              </div>
            </label>
            <input type="text" placeholder="验证码" value="" class="ui-input ui-input-checkcode" id="J-input-checkcode"
                   data-type="IMAGE" maxlength="4" name="checkCode" autocomplete="off" tabindex="3" data=""
                   seed="authcenter-input-checkcode" data-widget-cid="widget-7" data-explain="">
            <span class="sl-checkcode" id="J-checkcodeIcon"></span>
            <div class="ui-checkcode">
              <img class="ui-checkcode-img" id="J-checkcode-img"
                   src="https://authet15.alipay.com:443/login/imgcode.htm?sessionID=516f855cb56260cbddb237e8e9789155&amp;t=0.1421522489410908"
                   title="点击图片刷新验证码" alt="点击图片刷新验证码" seed="authcenter-img-checkcode">
              <div class="ui-checkcode-voice fn-hide" id="J-checkcode-voice"
                   data-src="https://authet15.alipay.com:443/login/audiocode.htm?sessionID=516f855cb56260cbddb237e8e9789155&amp;r=0.6355215870857888"
                   seed="authcenter-voice-checkcode">
                <span class="sl-process" id="J-checkcode-voice-bg"><i class="iconauth"></i></span>
                <span class="sl-refresh" id="J-checkcode-voice-txt"><i class="ui-icon ui-icon-voicing" title="播放中"></i>播放中...</span>
              </div>
            </div>
            <div class="ui-form-explain"></div>
          </div>
          <div class="ui-form-item ui-form-item-30pd" id="J-submit">
            <input type="submit" value="登 录" class="ui-button" id="J-login-btn">
            <p class="ui-form-other">
              <a class="register" href="https://memberprod.alipay.com/account/reg/index.htm" target="_blank" title="免费注册" tabindex="6">免费注册</a>
            </p>
          </div><!-- //submit -->
        </fieldset>
      </form>
    </div>
    </div>
  </div>
</template>

<script>

</script>

<style lang="css" scoped>
  .popbox .popmask {
    display: block;
    position: fixed;
    z-index: 997;
    top: 0;
    left: 0;
    width:  100%;
    height: 100%;
    background: rgba(0,0,0,0.6);
  }
  .popbox .loginbox {
    width: 286px;
    height: 380px;
    border-radius: 5px;
    overflow: hidden;
    position: absolute;
    z-index: 1001;
    top: 50%;
    left: 50%;
    margin-left: -143px;
    margin-top: -120px;
}
  .popbox .popbox-close { position: absolute; z-index: 9; top: 5px; left: 10px; font-size: 16px; color: #ccc; text-decoration: none;}
  .popbox .popbox-close:hover {color:#f1f1f1;}
  .login {
    width: 220px;
    padding: 0 31px 0 33px;
    position: relative;
    overflow: hidden;
    border: 1px solid #a7a7a7
  }
  .login a {
    color: #0AE
  }
  .login-modern {
    border: 1px solid transparent;
    background: rgba(0,0,0,.5);
    _background: 0 0;
    _border: 0;
    filter: progid:DXImageTransform.Microsoft.Gradient(GradientType=0, StartColorStr='#66000000', EndColorStr='#66000000');
  }
  :root .login-modern {
    filter: progid:DXImageTransform.Microsoft.Gradient(GradientType=0, StartColorStr='#00000000', EndColorStr='#00000000')\9
  }
.ui-form {
    font-size: 12px;
    line-height: 1.5;
    position: relative;
    zoom:1}

.ui-form,.ui-form * {
    list-style: none
}

.ui-form fieldset {
    border: 0;
    zoom:1}

.ui-form-title {
    font: 18px/28px tahoma,arial,"Hiragino Sans GB","Microsoft Yahei",\5b8b\4f53;
    font-weight: 500;
    font-weight: bold\0;
    *font-weight: 700;
    padding: 26px 0 16px;
    width: 100%;
    color: #4d4d4d;
    text-align: center
}

.login-modern .ui-form-title {
    color: #fff
}

.login-sso .ui-form-title {
    text-align: center
}

.ui-form-item:after {
    clear: both;
    content: '.';
    display: block;
    height: 0;
    visibility: hidden
}

.ui-form-item {
    padding: 0 0 10px;
    zoom:1;position: relative
}

.ui-form-item-20pd {
    padding-bottom: 18px
}

.ui-form-item-30pd {
    padding-bottom: 28px
}

.ui-form-item input {
    vertical-align: middle
}

.ui-form-other {
    position: relative;
    line-height: 18px;
    padding-top: 7px;
    height: 18px;
    zoom:1;_width: 100%;
    _overflow: hidden
}

.ui-form-other-fg {
    padding-top: 4px
}

.ui-form-other .textlink-ml20 {
    margin-left: 5px
}

.ui-form-other .forgot {
    position: absolute;
    right: 0;
    top: 5px
}

.ui-form-other .register {
    position: absolute;
    right: 0;
    top: 7px;
    font-size: 12px;
    color: #0AE
}

.ui-form-explain {
    display: none;
    height: 0;
    overflow: hidden
}

.ui-form-text {
    position: relative;
    line-height: 18px;
    height: 18px;
    font-size: 14px;
    padding-bottom: 10px;
    color: #4d4d4d;
    zoom:1}

.login-modern .ui-form-text {
    color: #fff;
    zoom:1}
.sl-error {
    position: relative;
    margin: 0;
    width: 212px;
    height: 0;
    opacity: .2;
    color: #4D4D4D;
    overflow: hidden;
    -webkit-transition-property: height,opacity;
    -webkit-transition-duration: .3s;
    -webkit-transition-timing-function: ease;
    -moz-transition-property: height,opacity;
    -moz-transition-duration: .3s;
    -moz-transition-timing-function: ease;
    transition-property: height,opacity;
    transition-duration: .3s;
    transition-timing-function: ease
}

.sl-error-display {
    margin: 35px auto 16px;
    padding: 3px 5px 3px 0;
    height: auto;
    opacity: 1;
    line-height: 26px;
    background: #FDEEE9;
    border: 1px solid #fadcd3
}

.sl-error .iconfont {
    display: none
}

.sl-error-display .iconfont {
    display: block;
    width: 20px;
    height: 20px;
    color: #f17975;
    line-height: 20px;
    position: absolute;
    top: 4px;
    left: 5px;
    font-size: 16px
}

.sl-error-display .sl-error-text {
    display: block;
    padding-left: 10px;
    line-height: 20px
}

.sl-error-display .sl-error-link {
    color: #08C;
    cursor: pointer
}

.sl-error-display .sl-error-link:hover {
}

.ui-label {
    width: 39px;
    height: 38px;
    display: block;
    float: left;
    cursor: pointer
}

.login .ui-label {
    border-top: 1px solid #a7a7a7;
    border-bottom: 1px solid #a7a7a7;
    border-left: 1px solid #a7a7a7
}

.login .ui-label:hover {
    border-top: 1px solid #6d6d6d;
    border-bottom: 1px solid #6d6d6d;
    border-left: 1px solid #6d6d6d
}

.ui-label .ui-icon {
    width: 39px;
    height: 38px;
    display: block;
    overflow: hidden;
    background-color: #aaabab;
    background-repeat: no-repeat;
    text-align: center;
    line-height: 38px
}

.ui-label:hover .ui-icon,.ui-label-hover .ui-icon {
    cursor: pointer;
    background-color: #6d6d6d
}
.ui-icon-userDEF {
    background-position: -2px 5px
}

.ui-icon-securityON {
    background-position: -42px 5px
}

.ui-icon-securityOFF {
    background-position: -84px 5px
}

.ui-icon-securityERR {
    background-position: -250px 6px
}

.ui-icon-checkcodeT {
    background-position: -126px 5px
}

.ui-icon-checkcodeV {
    background-position: -167px 5px
}
.iconauth {
    font-family: iconauth!important;
    font-size: 24px;
    font-style: normal;
    color: #FFF;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: .2px;
    -moz-osx-font-smoothing: grayscale
}

.ui-input {
    float: left;
    position: relative;
    padding: 9px;
    line-height: 20px;
    height: 20px;
    color: #595959;
    font-size: 12px;
    vertical-align: middle;
    *vertical-align: -5px;
    -webkit-border-radius: 0;
    -moz-border-radius: 0;
    border-radius: 0;
    box-shadow: none
}

.login .ui-input {
    border: 1px solid #a7a7a7
}

.login-modern .ui-input {
    border: 1px solid #fff
}

.ui-input-normal,.standardPwdContainer .ui-input,.alieditContainer .ui-input {
    width: 159px;
    _width: 157px
}

.ui-input-checkcode {
    width: 69px
}

.ui-input:hover,.ui-input-hover {
}

.ui-input:focus,.ui-input-focus {
    outline-style: none;
    color: #595959
}

.ui-input[disabled] {
    background: #f2f2f2
}

.ui-input:disabled {
    background: #f2f2f2
}

.placeholder {
    color: #ccc
}

.ui-input:-ms-input-placeholder {
    color: #ccc
}

.ui-form-item .alieditContainer {
    width: 179px;
    _width: 177px;
    height: 40px;
    display: inline-block;
    background: #fff;
    border: 0;
    _float: left
}
.sl-delect {
    cursor: pointer;
    position: absolute;
    width: 20px;
    height: 20px;
    top: 10px;
    right: 7px;
    display: block;
    line-height: 20px;
    text-align: center;
    font-size: 18px;
    z-index: 2;
    background: #fff
}

.sl-delect .iconfont {
    width: 20px;
    height: 20px;
    font-size: 18px;
    color: #ababab;
    cursor: pointer;
    line-height: 20px
}

.sl-delect:hover .iconfont,.sl-delect-hover .iconfont {
    color: #6d6d6d
}













  input.sixDigitPassword {
    position: absolute;
    color: #fff;
    opacity: 0;
    width: 1px;
    height: 1px;
    font-size: 1px;
    left: 0;
    -webkit-box-sizing: content-box;
    box-sizing: content-box;
    -webkit-user-select: initial; /* 取消禁用选择页面元素 */
    outline: none;
    margin-left: -9999px;
  }

  div.sixDigitPassword {
    cursor: text;
    background: #fff;
    outline: none;
    position: relative;
    padding: 8px 0;
    height: 14px;
    border: 1px solid #cccccc;
    border-radius: 2px;
  }

  div.sixDigitPassword i {
    float: left;
    display: block;
    padding: 4px 0;
    height: 7px;
    border-left: 1px solid #cccccc;
  }

  div.sixDigitPassword i.active {
    background-image: url("https://t.alipayobjects.com/images/rmsweb/T1nYJhXalXXXXXXXXX.gif");
    background-repeat: no-repeat;
    background-position: center center;
  }

  div.sixDigitPassword b {
    display: block;
    margin: 0 auto;
    width: 7px;
    height: 7px;
    overflow: hidden;
    visibility: hidden;
    background-image: url("https://t.alipayobjects.com/tfscom/T1sl0fXcBnXXXXXXXX.png");
  }

  div.sixDigitPassword span {
    position: absolute;
    display: block;
    left: 0px;
    top: -1px;
    height: 30px;
    border: 1px solid rgba(82, 168, 236, .8);
    border: 1px solid #00ffff \9;
    border-radius: 2px;
    visibility: hidden;
    -webkit-box-shadow: inset 0px 2px 2px rgba(0, 0, 0, 0.75), 0 0 8px rgba(82, 168, 236, 0.6);
    box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(82, 168, 236, 0.6);
  }
</style>
