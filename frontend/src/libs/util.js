let util = {

}

// 设置页面标题(meta)
util.title = function (title) {
  title = title ? title + '与你分享我的发现' : '爱分享_与你分享我的发现'
  window.document.title = title
}

// 判断参数是否是其中之一
util.oneOf = function (value, validList) {
  for (let i = 0; i < validList.length; i++) {
    if (value === validList[i]) {
      return true
    }
  }
  return false
}

export default util
