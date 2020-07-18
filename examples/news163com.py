# -*- coding: UTF-8 -*-
# !/usr/bin/env python
'''

author: MRN6

updated: Jul. 18th, 2020 Sat. 03:40PM

LICENSE: CC0

'''

news163html='''

 <!DOCTYPE HTML>
<!--[if IE 6 ]> <html id="ne_wrap" class="ne_ua_ie6 ne_ua_ielte8"> <![endif]-->
<!--[if IE 7 ]> <html id="ne_wrap" class="ne_ua_ie7 ne_ua_ielte8"> <![endif]-->
<!--[if IE 8 ]> <html id="ne_wrap" class="ne_ua_ie8 ne_ua_ielte8"> <![endif]-->
<!--[if IE 9 ]> <html id="ne_wrap" class="ne_ua_ie9"> <![endif]-->
<!--[if (gte IE 10)|!(IE)]><!--> <html id="ne_wrap" phone="1"> <!--<![endif]-->
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="model_url" content="http://news.163.com/special/index2015/" />
<title>网易新闻</title>
<base target="_blank" />
<meta name="keywords" content="新闻,新闻中心,新闻频道,时事报道" />
<meta name="description" content="新闻,新闻中心,包含有时政新闻,国内新闻,国际新闻,社会新闻,时事评论,新闻图片,新闻专题,新闻论坛,军事,历史,的专业时事报道门户网站" />
  <script type="text/javascript" _keep="true">
    var matchStr =window.location.href;
    var reURL = /^(https):\/\/.+$/;
    if(!reURL.test(matchStr)){
        window.location.href = "https://news.163.com/";
    }
  </script>
<!-- 适配3g ie8bug-->
<!-- 广告样式 -->
<style>
.channel_relative_2016{
    position:relative;
    line-height: 0px;
}
.channel_relative_2016_lh{
    line-height: 0px;
}
.channel_ad_2016{
    height: 17px;
    display:none;
    background: rgba(0,0,0,0.6);
    background: #000\9;
    color: #fff;
    border-radius: 0 8px 0px 0px;
    line-height: 17px;
    width: 30px;
    text-align: left;
    overflow: hidden;
    font-size: 12px;
    font-family: Arial;
    position:absolute;
    left:0;
    bottom:0;
    z-index:3;
}
.channel_ad_text_2016{
    position: absolute;
    right: 1px;
    bottom: -2px;
    color: #999999;
    z-index:3;
    font-size: 12px;
    font-family: Arial;
   display:none;
  line-height: 18px;
}
.channel_relative_2016 .channel_ad_2016,.channel_relative_2016 .channel_ad_text_2016{
    display: inline-block;
}
</style>
<!-- channel2019_logo样式 -->
<style type="text/css">
	.channel2019_logo{
		/* https://cms-bucket.ws.126.net/2019/04/25/09e37a6a4dd349468cd38dd79a3b15b7.png */
        background: url(http://cms-bucket.ws.126.net/2020/0526/7d04acc7p00qaxfdz002vc0005x028kc.png) no-repeat !important;
		width: 152px !important;
		height: 37px !important;
		display: block !important;
		float: left!important;
	}
	/*新闻*/
	.channel2019_news_logo{
		background-position: 0px 4px !important;
	}
	/*科技*/
	.channel2019_tech_logo{
		background-position: 0px -96px !important;
    	
	}
	/*手机*/
	.channel2019_mobile_logo{
		background-position: 0px -196px !important;
		
	}
	/*数码*/
	.channel2019_digi_logo{
		background-position: 0px -296px !important;
    	
	}
	/*新闻学院*/
	.channel2019_college_logo{
		background-position: 0px -396px !important;
		width: 213px !important;
	}
	/*政务*/
	.channel2019_gov_logo{
		background-position: 0px -496px !important;
	}
	/*军事*/
	.channel2019_war_logo{
		background-position: 0px 0px !important;
    	height: 33px !important;
	}
	/*航空*/
	.channel2019_air_logo{
		background-position: 0px 0px !important;
    	height: 33px !important;
	}
   /*新闻排行榜*/
	.channel2019_newsrank_logo{
		background-position: 0px 0px !important;
    	height: 33px !important;
	}
  	/*新闻图片*/
	.channel2019_newsphoto_logo{
		background-position: 0px -2200px !important;
      	width: 213px !important;
    	height: 33px !important;
	}
	/*体育*/
	.channel2019_sports_logo{
		background-position: 0px -796px !important;
	}
  	/*体育二级页*/
	.channel2019_sportssub_logo{
		height: 33px !important;
		background-position: 0px -800px !important;
	}
	/*娱乐*/
	.channel2019_ent_logo{
		background-position: 0px -896px !important;
	}
	/*音乐*/
	.channel2019_music_logo{
		background-position: 0px -900px !important;
    	height: 32px !important;
	}
	/*时尚*/
	.channel2019_fashion_logo{
		background-position: 0px -1100px !important;
		height: 32px !important;
	}
	/*女人*/
	.channel2019_lady_logo{
		background-position: 0px -1196px !important;
	}
	/*财经*/
	.channel2019_money_logo{
		background-position: 0px -1300px !important;
	}
    /*手机图片*/
	.channel2019_mobilephoto_logo{
		background-position: 0px -2300px !important;
		width: 213px !important;
    	height: 33px !important;
	}
	/*汽车*/
	.channel2019_auto_logo{
		background-position: 0px -1396px !important;
	}
	/*旅游*/
	.channel2019_travel_logo{
		background-position: 0px -1496px !important;
	}
	/*健康*/
	.channel2019_jiankang_logo{
		background-position: 0px -1596px !important;
	}
	/*教育*/
	.channel2019_edu_logo{
		background-position: 0px -1696px !important;
	}
	/*艺术*/
	.channel2019_art_logo{
		background-position: 0px -1796px !important;
	}
	/*亲子*/
	.channel2019_baby_logo{
		background-position: 0px -1896px !important;
	}
	/*双创*/
	.channel2019_shuangchuang_logo{
		background-position: 0px -1996px !important;
	}
	/*酒香*/
	.channel2019_jiu_logo{
		background-position: 0px -2096px !important;
	}
  	/*游戏*/
	.channel2019_game_logo{
		background-position: 0px -2400px !important;
	}
    /*房产*/
	.channel2019_house_logo{
		background-position: 0px -2496px !important;
	}
    /*家居*/
	.channel2019_home_logo{
		background-position: 0px -2596px !important;
	}
	</style>
<script type="text/javascript" _keep="true">
(function() {
    if(/s=noRedirect/i.test(location.search)) return; 
    if(/AppleWebKit.*Mobile/i.test(navigator.userAgent) || (/MIDP|SymbianOS|NOKIA|SAMSUNG|LG|NEC|TCL|Alcatel|BIRD|DBTEL|Dopod|PHILIPS|HAIER|LENOVO|MOT-|Nokia|SonyEricsson|SIE-|Amoi|ZTE/.test(navigator.userAgent))) {
        try {
            if(/Android|Windows Phone|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)) {
                 window.location.href = "https://3g.163.com/touch/news/";
            } else if(/iPad/i.test(navigator.userAgent)) {
                window.location.href = "https://news.163.com/pad/"
            }
        } catch(e) {}
    }   
})();
</script>
	<link rel="stylesheet" href="https://static.ws.126.net/163/f2e/news/index2016_rmd/css/head~bbb97b2a2256c.css">
</head>
<body class="news_pc" ne-module="/news/index2016_rmd/index2016.js" ne-class="{{myState.isNs9 ? 'ns9' : 'ns12'}}" ne-plugin="/modules/plugins/lazyload/lazyload.js">
<div class="index2016_wrap" id="index2016_wrap">
    <div >
        <!-- 节日动画 start -->
                <!-- 节日动画 end -->
        <div class="common_nav">
        <link rel="stylesheet" href="//static.ws.126.net/163/f2e/commonnav2019/css/commonnav_headcss-e017654fb2.css"/>
<!-- urs -->
<script _keep="true" src="https://urswebzj.nosdn.127.net/webzj_cdn101/message.js" type="text/javascript"></script>
<div class="ntes_nav_wrap" id="js_N_NTES_wrap">
  <div class="ntes-nav" id="js_N_nav">
    <div class="ntes-nav-main clearfix">
            <div class="c-fl">
        <a class="ntes-nav-index-title ntes-nav-entry-wide c-fl" href="http://www.163.com/" title="网易首页">网易首页</a>
        <!-- 应用 -->
        <div class="js_N_navSelect ntes-nav-select ntes-nav-select-wide ntes-nav-app  c-fl">
          <a href="http://www.163.com/#f=topnav" class="ntes-nav-select-title ntes-nav-entry-bgblack JS_NTES_LOG_FE">应用
            <em class="ntes-nav-select-arr"></em>
          </a>
          <div class="ntes-nav-select-pop">
            <ul class="ntes-nav-select-list clearfix">
              <li>
                <a href="http://m.163.com/newsapp/#f=topnav">
                  <span>
                    <em class="ntes-nav-app-newsapp">网易新闻</em>
                  </span>
                </a>
              </li>
              <li>
                <a href="http://open.163.com/#f=topnav">
                  <span>
                    <em class="ntes-nav-app-open">网易公开课</em>
                  </span>
                </a>
              </li>
              <li>
                <a href="https://hongcai.163.com/?from=pcsy-button">
                  <span>
                    <em class="ntes-nav-app-hongcai">网易红彩</em>
                  </span>
                </a>
              </li>              
              <li>
                <a href="https://gulu.163.com">
                  <span>
                    <em class="ntes-nav-app-gulu-video">网易新闻视频版</em>
                  </span>
                </a>
              </li>
              <li>
                <a href="http://u.163.com/aosoutbdbd8">
                  <span>
                    <em class="ntes-nav-app-yanxuan">网易严选</em>
                  </span>
                </a>
              </li>
              <li>
                <a href="http://mail.163.com/client/dl.html?from=mail46">
                  <span>
                    <em class="ntes-nav-app-mail">邮箱大师</em>
                  </span>
                </a>
              </li>
              <li class="last">
                <a href="http://study.163.com/client/download.htm?from=163app&utm_source=163.com&utm_medium=web_app&utm_campaign=business">
                  <span>
                    <em class="ntes-nav-app-study">网易云课堂</em>
                  </span>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="c-fr">
        <!-- 片段开始 -->
        <div class="ntes-nav-quick-navigation">
          <a href="javascript:void(0);" class="ntes-nav-quick-navigation-btn" id="js_N_ntes_nav_quick_navigation_btn" target="_self">
            <em>快速导航
              <span class="menu1"></span>
              <span class="menu2"></span>
              <span class="menu3"></span>
            </em>
          </a>
          <div class="ntes-quicknav-pop" id="js_N_ntes_quicknav_pop">
            <div class="ntes-quicknav-list">
              <div class="ntes-quicknav-content">
                <ul class="ntes-quicknav-column ntes-quicknav-column-1">
                  <li>
                  <h3><a href="https://news.163.com">新闻</a></h3>
                  </li>
                  <li>
                  <a href="http://news.163.com/domestic">国内</a>
                  </li>
                  <li>
                  <a href="http://news.163.com/world">国际</a>
                  </li>
                  <li>
                  <a href="http://news.163.com/photo">图片</a>
                  </li>
                  <li>
                  <a href="http://view.163.com">评论</a>
                  </li>
                  <li>
                  <a href="http://discovery.163.com">探索</a>
                  </li>
                  <li>
                  <a href="http://war.163.com">军事</a>
                  </li>
                  <li>
                  <a href="http://news.163.com/localnews/">本地新闻</a>
                  </li>
                  <li>
                  <a href="http://news.163.com/special/wangsansanhome/">王三三</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-2">
                  <li>
                  <h3><a href="http://sports.163.com">体育</a></h3>
                  </li>
                  <li>
                  <a href="http://sports.163.com/nba">NBA</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/cba">CBA</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/allsports">综合</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/zc">中超</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/world">国际足球</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/yc">英超</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/xj">西甲</a>
                  </li>
                  <li>
                  <a href="http://sports.163.com/yj">意甲</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-3">
                  <li>
                  <h3><a href="http://ent.163.com">娱乐</a></h3>
                  </li>
                  <li>
                  <a href="http://ent.163.com/star">明星</a>
                  </li>
                  <li>
                  <a href="http://ent.163.com/photo">图片</a>
                  </li>
                  <li>
                  <a href="http://ent.163.com/movie">电影</a>
                  </li>
                  <li>
                  <a href="http://ent.163.com/tv">电视</a>
                  </li>
                  <li>
                  <a href="http://ent.163.com/music">音乐</a>
                  </li>
                  <li>
                  <a href="http://ent.163.com/special/gsbjb/">稿事编辑部</a>
                  </li>
                  <li>
                  <a href="http://ent.163.com/special/focus_ent/">娱乐FOCUS</a>
                  </li>
                  <li><a href="http://ent.163.com/special/xbkhz/">星捕快</a></li> 
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-4">
                  <li>
                  <h3><a href="http://money.163.com">财经</a></h3>
                  </li>
                  <li>
                  <a href="http://money.163.com/stock">股票</a>
                  </li>
                  <li>
                  <a href="http://quotes.money.163.com/stock">行情</a>
                  </li>
                  <li>
                  <a href="http://money.163.com/chanjing">产经</a>
                  </li>
                  <li>
                  <a href="http://money.163.com/ipo">新股</a>
                  </li>
                  <li>
                  <a href="http://money.163.com/finance">金融</a>
                  </li>
                  <li>
                  <a href="http://money.163.com/fund">基金</a>
                  </li>
                  <li>
                  <a href="http://biz.163.com">商业</a>
                  </li>
                  <li>
                  <a href="http://money.163.com/licai">理财</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-5">
                  <li>
                  <h3><a href="http://auto.163.com">汽车</a></h3>
                  </li>
                  <li>
                  <a href="http://auto.163.com/buy">购车</a>
                  </li>
                  <li>
                  <a href="http://auto.163.com/depreciate">行情</a>
                  </li>
                  <li>
                  <a href="http://product.auto.163.com/finder">选车</a>
                  </li>
                  <li>
                  <a href="http://product.auto.163.com">车型库</a>
                  </li>
                  <li>
                  <a href="http://auto.163.com/news">行业</a>
                  </li>
                  <li>
                  <a href="http://auto.163.com/chezhu">用车</a>
                  </li>
                  <li>
                  <a href="http://auto.163.com/photo">汽车图片</a>
                  </li>
                  <li>
                  &nbsp;
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-6">
                  <li>
                  <h3><a href="http://tech.163.com">科技</a></h3>
                  </li>
                  <li>
                  <a href="http://tech.163.com/telecom/">通信</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/it">IT</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/internet">互联网</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/special/ydhlw">移动互联网</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/special/chzt">特别策划</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/special/wudaokou">五道口沙龙</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/special/yyzd">易语中的</a>
                  </li>
                  <li>
                  <a href="http://tech.163.com/special">专题</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-7">
                  <li>
                  <h3><a href="http://lady.163.com">女人</a></h3>
                  </li>
                  <li>
                  <a href="http://baby.163.com">亲子</a>
                  </li>
                  <li>
                  <a href="http://fashion.163.com/art">艺术</a>
                  </li>
                  <li>
                  <a href="http://fashion.163.com">时尚</a>
                  </li>
                  <li>
                  <a href="http://shoucang.163.com">收藏</a>
                  </li>
                  <li>
                  <a href="http://lady.163.com/sense">情感</a>
                  </li>
                  <li>
                  <a href="http://lady.163.com/astro">星座</a>
                  </li>
                  <li>
                  <a href="http://lady.163.com/beauty">美容</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-8">
                  <li>
                  <h3><a href="http://mobile.163.com">手机</a><span>/</span><a href="http://digi.163.com/">数码</a></h3>
                  </li>
                  <li>
                  <a href="http://mobile.163.com/mi">移动</a>
                  </li>
                  <li>
                  <a href="http://digi.163.com/pc">电脑</a>
                  </li>
                  <li>
                  <a href="http://product.mobile.163.com">手机库</a>
                  </li>
                  <li>
                  <a href="http://hea.163.com/">家电</a>
                  </li>
                  <li>
                  <a href="http://digi.163.com/smart">智能硬件</a>
                  </li>
                  <li>
                  <a href="http://digi.163.com/dc">相机</a>
                  </li>
                  <li>
                  <a href="http://v.mobile.163.com">手机视频</a>
                  </li>
                  <li>
                  &nbsp;
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-9">
                  <li>
                  <h3><a href="http://house.163.com">房产</a><span>/</span><a href="http://home.163.com">家居</a></h3>
                  </li>
                  <li>
                  <a href="http://bj.house.163.com">北京房产</a>
                  </li>
                  <li>
                  <a href="http://sh.house.163.com">上海房产</a>
                  </li>
                  <li>
                  <a href="http://gz.house.163.com">广州房产</a>
                  </li>
                  <li>
                  <a href="http://house.163.com/city">全部分站</a>
                  </li>
                  <li>
                  <a href="http://xf.house.163.com">楼盘库</a>
                  </li>
                  <li>
                  <a href="http://home.163.com/jiaju/">家具</a>
                  </li>
                  <li>
                  <a href="http://home.163.com/weiyu/">卫浴</a>
                  </li>
                  <li>
                  <a href="http://home.163.com/special/jiajuyigui">衣柜</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-10">
                  <li>
                  <h3><a href="http://travel.163.com">旅游</a></h3>
                  </li>
                  <li>
                  <a href="http://travel.163.com/outdoor">户外</a>
                  </li>
                  <li>
                  <a href="http://guizhou.travel.163.com">贵州</a>
                  </li>
                  <li>
                  <a href="http://travel.163.com/food">美食</a>
                  </li>
                  <li>
                  <a href="http://jingdian.travel.163.com/domestic/1000066937">四川</a>
                  </li>
                  <li>
                  <a href="http://jingdian.travel.163.com">景点</a>
                  </li>
                  <li>
                  <a href="http://jingdian.travel.163.com/domestic/1000066944">新疆</a>
                  </li>
                  <li>
                  <a href="http://travel.163.com/special/travellist/#f=endnav">专题</a>
                  </li>
                  <li>
                  <a href="http://jingdian.travel.163.com/domestic/1000066926/#f=endnav">西藏</a>
                  </li>
                </ul>
                <ul class="ntes-quicknav-column ntes-quicknav-column-11">
                  <li>
                  <h3><a href="http://edu.163.com">教育</a></h3>
                  </li>
                  <li>
                  <a href="http://edu.163.com/yimin">移民</a>
                  </li>
                  <li>
                  <a href="http://edu.163.com/kaoyan">考研</a>
                  </li>
                  <li>
                  <a href="http://edu.163.com/liuxue">留学</a>
                  </li>
                  <li>
                  <a href="http://edu.163.com/special/official">公务员</a>
                  </li>
                  <li>
                  <a href="http://edu.163.com/en">外语</a>
                  </li>
                  <li>
                  <a href="http://kids.163.com">中小学</a>
                  </li>
                  <li>
                  <a href="http://edu.163.com/gaokao">高考</a>
                  </li>
                  <li>
                  <a href="http://daxue.163.com">校园</a>
                  </li>
                </ul>
                <div class="ntes-nav-sitemap"><a href="http://sitemap.163.com/"><i></i>查看网易地图</a></div>
              </div>
            </div>
          </div>
        </div>
        <div class="c-fr">
          <div class="c-fl" id="js_N_navLoginBefore">
            <div id="js_N_navHighlight" class="js_loginframe ntes-nav-login ntes-nav-login-normal">
              <a href="http://reg.163.com/" class="ntes-nav-login-title" id="js_N_nav_login_title">登录</a>
              <div class="ntes-nav-loginframe-pop" id="js_N_login_wrap">
                <!--加载登陆组件-->
              </div>
            </div>
            <div class="js_N_navSelect ntes-nav-select ntes-nav-select-wide  JS_NTES_LOG_FE c-fl">
              <a class="ntes-nav-select-title ntes-nav-select-title-register" href="https://mail.163.com/register/index.htm?from=163navi&regPage=163">注册免费邮箱
                <em class="ntes-nav-select-arr"></em>
              </a>
              <div class="ntes-nav-select-pop">
                <ul class="ntes-nav-select-list clearfix" style="width:210px;">
                  <li>
                    <a href="https://reg1.vip.163.com/newReg1/reg?from=new_topnav&utm_source=new_topnav">
                      <span style="width:190px;">注册VIP邮箱（特权邮箱，付费）</span>
                    </a>
                  </li>
                  <li class="last JS_NTES_LOG_FE">
                    <a href="http://mail.163.com/client/dl.html?from=mail46">
                      <span style="width:190px;">免费下载网易官方手机邮箱应用</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div class="c-fl" id="js_N_navLoginAfter" style="display:none">
            <div id="js_N_logined_warp" class="js_N_navSelect ntes-nav-select ntes-nav-logined JS_NTES_LOG_FE">
              <span class="ntes-nav-select-title ntes-nav-logined-userinfo">
                <span id="js_N_navUsername" class="ntes-nav-logined-username"></span>
                <em class="ntes-nav-select-arr"></em>
              </span>
              <div id="js_login_suggest_wrap" class="ntes-nav-select-pop">
                <ul id="js_logined_suggest" class="ntes-nav-select-list clearfix"></ul>
              </div>
            </div>
            <a class="ntes-nav-entry-wide c-fl" target="_self" id="js_N_navLogout">安全退出</a>
          </div>
        </div>
        <ul class="ntes-nav-inside">
          <li>
            <div class="js_N_navSelect ntes-nav-select c-fl">
              <a href="http://www.163.com/newsapp/#f=163nav" class="ntes-nav-mobile-title ntes-nav-entry-bgblack">
                <em class="ntes-nav-entry-mobile">移动端</em>
              </a>
              <div class="qrcode-img">
                <a href="http://www.163.com/newsapp/#f=163nav">
                  <img src="//static.ws.126.net/f2e/include/common_nav/images/topapp.jpg">
                </a>
              </div>
            </div>
          </li>
          <li>
            <div class="js_N_navSelect ntes-nav-select c-fl">
              <a id="js_love_url" href="https://open.163.com/" class="ntes-nav-select-title ntes-nav-select-title-huatian ntes-nav-entry-bgblack">
                <em class="ntes-nav-entry-huatian">网易公开课</em>
                <em class="ntes-nav-select-arr"></em>
                <span class="ntes-nav-msg">
                  <em class="ntes-nav-msg-num"></em>
                </span>
              </a>
              <div class="ntes-nav-select-pop ntes-nav-select-pop-huatian">
                <ul class="ntes-nav-select-list clearfix">
                  <li>
                    <a href="https://vip.open.163.com">
                      <span>付费精品</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://open.163.com/ted/">
                      <span>TED</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://open.163.com/ocw/">
                      <span>国际名校公开课</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://open.163.com/cuvocw/">
                      <span>中国大学视频公开课</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://open.163.com/appreciation">
                      <span>赏课</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://open.163.com/khan/">
                      <span>可汗学院</span>
                    </a>
                  </li>
                  <li class="last">
                    <a href="http://open.163.com/special/appdownload_pc/">
                      <span>下载公开课</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <div class="js_N_navSelect ntes-nav-select c-fl">
              <a id="js_lofter_icon_url" href="http://you.163.com/?from=web_fc_menhu_xinrukou_1" class="ntes-nav-select-title ntes-nav-select-title-lofter ntes-nav-entry-bgblack">
                <em class="ntes-nav-entry-lofter">网易严选</em>
                <em class="ntes-nav-select-arr"></em>
                <span class="ntes-nav-msg" id="js_N_navLofterMsg">
                  <em class="ntes-nav-msg-num"></em>
                </span>
              </a>
              <div class="ntes-nav-select-pop ntes-nav-select-pop-lofter">
                <ul id="js_lofter_pop_url" class="ntes-nav-select-list clearfix">
                  <li>
                    <a href="https://act.you.163.com/act/pub/ABuyLQKNmKmK.html?from=planEE460F5FA536DE23plan&channel_type=2">
                      <span>爆品新人特价包邮</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/manufacturer/list?from=web_fc_menhu_xinrukou_3">
                      <span>品牌制造商爆款</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/item/recommend?from=web_fc_menhu_xinrukou_4">
                      <span>999+人气好评品</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/flashSale/index?from=web_fc_menhu_xinrukou_5">
                      <span>限时特惠</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/item/list?categoryId=1005000&from=web_fc_menhu_xinrukou_7">
                      <span>居家床品</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/item/list?categoryId=1005001&from=web_fc_menhu_xinrukou_8">
                      <span>精致餐厨</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/item/list?categoryId=1008000&from=web_fc_menhu_xinrukou_9">
                      <span>箱包鞋类</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://you.163.com/item/list?categoryId=1010000&from=web_fc_menhu_xinrukou_10">
                      <span>经典服饰</span>
                    </a>
                  </li>
                  <li class="last">
                    <a href="http://you.163.com/item/list?categoryId=1005002&from=web_fc_menhu_xinrukou_11">
                      <span>健康美食</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <div class="js_N_navSelect ntes-nav-select c-fl">
              <a href="http://pay.163.com/" class="ntes-nav-select-title
        ntes-nav-select-title-money ntes-nav-entry-bgblack">
                <em class="ntes-nav-entry-money">支付</em>
                <em class="ntes-nav-select-arr"></em>
              </a>
              <div class="ntes-nav-select-pop ntes-nav-select-pop-temp">
                <ul class="ntes-nav-select-list clearfix">
                  <li>
                    <a href="http://pay.163.com/#f=topnav">
                      <span>一卡通充值</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://ecard.163.com/script/index#f=topnav">
                      <span>一卡通购买</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://k.163.com/?product=163&trackid=01">
                      <span>网易白金卡</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://epay.163.com/">
                      <span>我的网易支付</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://3c.163.com/?from=wangyimenhu16">
                      <span>网易智造</span>
                    </a>
                  </li>
                  <li class="last">
                    <a href="http://lq.163.com?from=neteasemoney">
                      <span>网易来钱-借现金</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <div class="js_N_navSelect ntes-nav-select c-fl">
              <a href="http://baoxian.163.com/car/?from=mhgwc" class="ntes-nav-select-title
        ntes-nav-select-title-cart ntes-nav-entry-bgblack">
                <em class="ntes-nav-entry-cart">电商</em>
                <em class="ntes-nav-select-arr"></em>
              </a>
              <div class="ntes-nav-select-pop ntes-nav-select-pop-temp">
                <ul class="ntes-nav-select-list clearfix">
                  <li>
                    <a href="http://you.163.com?from=web_in_wydaohang">
                      <span>严选</span>
                    </a>
                  </li>
                  <li class="last">
                    <a href="http://lq.163.com?from=neteasebuy">
                      <span>我要借钱</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li>
          <li>
            <div class="js_N_navSelect ntes-nav-select c-fl">
              <a id="js_mail_url" class="ntes-nav-select-title
        ntes-nav-select-title-mail ntes-nav-entry-bgblack">
                <em class="ntes-nav-entry-mail">邮箱</em>
                <em class="ntes-nav-select-arr"></em>
                <span class="ntes-nav-msg" id="js_N_navMailMsg">
                  <em class="ntes-nav-msg-num" id="js_N_navMailMsgNum"></em>
                </span>
              </a>
              <div class="ntes-nav-select-pop ntes-nav-select-pop-mail">
                <ul class="ntes-nav-select-list clearfix">
                  <li>
                    <a href="http://email.163.com/#f=topnav">
                      <span>免费邮箱</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://vipmail.163.com/#f=topnav">
                      <span>VIP邮箱</span>
                    </a>
                  </li>
                  <li>
                    <a href="http://qiye.163.com/#f=topnav">
                      <span>企业邮箱</span>
                    </a>
                  </li>
                  <li>
                    <a href="https://mail.163.com/register/index.htm?from=ntes_nav&regPage=163">
                      <span>免费注册</span>
                    </a>
                  </li>
                  <li class="last">
                    <a href="http://mail.163.com/dashi/dlpro.html?from=mail46">
                      <span>客户端下载</span>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</div>
<script src="//static.ws.126.net/163/f2e/commonnav2019/js/commonnav_headjs-125e1cbda2.js"></script>
        </div>
        <!-- 节日背景 -->
        <div class="ns-bg-wrap">
            
<div class="N-nav-channel JS_NTES_LOG_FE" data-module-name="xwwzy_11_headdaohang">
    <a class="first" href="https://news.163.com/">新闻</a><a href="http://sports.163.com/">体育</a><a href="http://sports.163.com/nba/">NBA</a><a href="http://ent.163.com/">娱乐</a><a href="http://money.163.com/">财经</a><a href="http://money.163.com/stock/">股票</a><a id="_link_auto" href="http://auto.163.com/">汽车</a><a href="http://tech.163.com/">科技</a><a href="http://mobile.163.com/">手机</a><a href="http://tech.163.com/smart/">智能</a><a href="http://lady.163.com/">女人</a><a href="http://v.163.com/">直播</a><a href="http://v.163.com/special/video/#tuijian">视频</a><a href="http://travel.163.com/">旅游</a><a id="houseUrl" href="http://house.163.com/">房产</a><a href="http://home.163.com/" id="homeUrl">家居</a><a href="http://edu.163.com/">教育</a><a href="http://book.163.com/">读书</a><a id="_link_game" href="https://news.163.com/">本地</a><a href="http://jiankang.163.com/">健康</a><a class="last" href="http://art.163.com/">艺术</a>
</div>
<!-- 游戏替换为本地，并定向 0310-->
<!-- 配置定向城市 -->
<script type="text/javascript" _keep="true">
var HouseNavBendiTxt = {
    "province": [
        {
            "name": "北京市",
            "shortName": "北京",
            "url":"http://bj.news.163.com/"
        },
        {
            "name": "上海市",
            "shortName": "上海",
            "url":"http://sh.news.163.com/"
        },
        {
            "name": "天津市",
            "shortName": "天津",
            "url":"http://tj.news.163.com/"
        },
        {
            "name": "广东省",
            "shortName": "广东",
            "url":"http://gd.news.163.com/"
        },
        {
            "name": "江苏省",
            "shortName": "江苏",
            "url":"http://js.news.163.com/"
        },
        {
            "name": "浙江省",
            "shortName": "浙江",
            "url":"http://zj.news.163.com/"
        },
        {
            "name": "四川省",
            "shortName": "四川",
            "url":"http://sc.news.163.com/"
        },
        {
            "name": "黑龙江省",
            "shortName": "黑龙江",
            "url":"http://hlj.news.163.com/"
        },
        {
            "name": "吉林省",
            "shortName": "吉林",
            "url":"http://jl.news.163.com/"
        },
        {
            "name": "辽宁省",
            "shortName": "辽宁",
            "url":"http://liaoning.news.163.com/"
        },
        {
            "name": "内蒙古自治区",
            "shortName": "内蒙古",
            "url":"http://hhht.news.163.com/"
        },
        {
            "name": "河北省",
            "shortName": "河北",
            "url":"http://hebei.news.163.com/"
        },
        {
            "name": "河南省",
            "shortName": "河南",
            "url":"http://henan.163.com/"
        },
        {
            "name": "山东省",
            "shortName": "山东",
            "url":"http://sd.news.163.com/"
        },
        {
            "name": "陕西省",
            "shortName": "陕西",
            "url":"http://shanxi.news.163.com/"
        },
        {
            "name": "甘肃省",
            "shortName": "甘肃",
            "url":"http://gs.news.163.com/"
        },
        {
            "name": "宁夏回族自治区",
            "shortName": "宁夏",
            "url":"http://ningxia.news.163.com/"
        },
        {
            "name": "新疆维吾尔自治区",
            "shortName": "新疆",
            "url":"http://xj.news.163.com/"
        },
        {
            "name": "安徽省",
            "shortName": "安徽",
            "url":"http://ah.news.163.com/"
        },
        {
            "name": "福建省",
            "shortName": "福建",
            "url":"http://fj.news.163.com/"
        },
        {
            "name": "广西壮族自治区",
            "shortName": "广西",
            "url":"http://gx.news.163.com/"
        },
        {
            "name": "重庆市",
            "shortName": "重庆",
            "url":"http://chongqing.163.com/"
        },
        {
            "name": "湖北省",
            "shortName": "湖北",
            "url":"http://hb.news.163.com/"
        },
        {
            "name": "江西省",
            "shortName": "江西",
            "url":"http://jx.news.163.com/"
        },
        {
            "name": "海南省",
            "shortName": "海南",
            "url":"http://hn.news.163.com/"
        },
        {
            "name": "贵州省",
            "shortName": "贵州",
            "url":"http://gz.news.163.com/"
        },
        {
            "name": "云南省",
            "shortName": "云南",
            "url":"http://yn.news.163.com/"
        },
        {
            "name": "湖南省",
            "shortName": "上海",
            "url":"http://sh.news.163.com/"
        },
        {
            "name": "山西省",
            "shortName": "山西",
            "url":"http://sx.news.163.com"
        },
        {
            "name": "西藏自治区",
            "shortName": "北京",
            "url":"http://bj.news.163.com/"
        },
        {
            "name": "香港特别行政区",
            "shortName": "广东",
            "url":"http://gd.news.163.com/"
        },
        {
            "name": "澳门特别行政区",
            "shortName": "广东",
            "url":"http://gd.news.163.com/"
        },
        {
            "name": "台湾省",
            "shortName": "广东",
            "url":"http://gd.news.163.com/"
        },
        {
            "name": "天津市",
            "shortName": "北京",
            "url":"http://bj.news.163.com/"
        },
        {
            "name": "青海省",
            "shortName": "北京",
            "url":"http://bj.news.163.com/"
        }
    ],
    "city": [
        {
            "name": "大连市",
            "shortName": "大连",
            "url":"http://dl.news.163.com"
        },
        {
            "name": "青岛市",
            "shortName": "青岛",
            "url":"http://qingdao.news.163.com"
        },
        {
            "name": "宁波市",
            "shortName": "宁波",
            "url":"http://ningbo.news.163.com"
        },
        {
            "name": "厦门市",
            "shortName": "厦门",
            "url":"http://xiamen.news.163.com"
        },
        {
            "name": "深圳市",
            "shortName": "深圳",
            "url":"http://shenzhen.news.163.com/"
        }
    ],
    "defalt": {
            "name": "",
            "shortName": "本地",
            "url":"http://news.163.com/"
        }
};
</script>
<script type="text/javascript" _keep="true">
    //本地设置定向省份
    function setBendiName(){
        var js_nav_bendi = document.getElementById("_link_game");
        var cityname = "";
        var cityurl = "";
        var _loc = window.localAddress;
        if(!js_nav_bendi)
            return;
        if(HouseNavBendiTxt.city && _loc){
            var citylist = HouseNavBendiTxt.city;
            var localcity = _loc.city;
            for(var i=0;i<citylist.length;i++){
                if(citylist[i].name == localcity){
                    cityname = citylist[i].shortName;
                    cityurl = citylist[i].url;
                    break;
                }
            }
        }
        if(cityname == "" && cityurl == "" && HouseNavBendiTxt.province && _loc){
            var provincelist = HouseNavBendiTxt.province;
            var localprovince = _loc.province;
            for(var i=0;i<provincelist.length;i++){
                if(provincelist[i].name == localprovince){
                    cityname = provincelist[i].shortName;
                    cityurl = provincelist[i].url;
                    break;
                }
            }
        }
        if(js_nav_bendi && cityname != "" && cityurl != ""){
            js_nav_bendi.innerHTML = cityname;
            js_nav_bendi.href = cityurl;
        }
        if(js_nav_bendi && cityname == "" && cityurl == ""){
            js_nav_bendi.innerHTML = "本地";
            js_nav_bendi.href = "http://news.163.com";
        }
    }
    function BENDI_NAV_CALLBACK(data){
       if(data && data.result){
            if(window.HouseNavBendiTxt){
                window.localAddress = data.result;
                setBendiName();
            } 
       }
    };
    
    if(window.localAddress){
        if(window.HouseNavBendiTxt){
            setBendiName();
        } 
    }else{
        var url = "//ipservice.163.com/locate/api/getLocByIp?key=C6E22B7D480E3312C74EC7EF013E50C5&callback=BENDI_NAV_CALLBACK";
        var script = document.createElement('script');
        script.setAttribute('src', url);
        document.getElementsByTagName('head')[0].appendChild(script);
    }
</script>
            <div class="index2016_content">
                <!-- 头部广告 开始-->
                <div class="ns_area index_top_ad channel_relative_2016">
                    <!--16新闻首页顶通-->
<div class="at_item common_ad_item top_ad_column" adType="topColumnAd" requestUrl="https://nex.163.com/q?app=7BE0FC82&c=news&l=11&site=netease&affiliate=news&cat=homepage&type=column1200x125_960x100&location=10"></div>
<span class="channel_ad_2016">广告</span>
                </div>
                <!-- 头部广告 结束-->
                <!-- 头部导航 开始-->
                <div class="index_head">
                    <div class="ns_area hd">
                        <h1>    
                            <a href="https://news.163.com/" class="channel2019_logo channel2019_news_logo">网易新闻有态度</a>
                        </h1>
                    </div>
                    <div class="bd">
                        <div class="ns_area list">
                        <ul>
     <li class="first"><a href="http://www.163.com/">首页</a></li>
     <li><a href="http://news.163.com/rank/">排行</a></li>
     <li><a href="http://news.163.com/photo/#Current">图片</a></li>
     <li class="menu_guonei"><a href="http://news.163.com/domestic/">国内</a></li>
     <li class="menu_guoji"><a href="http://news.163.com/world/">国际</a></li>
     <!--<li class="menu_shehui"><a href="http://news.163.com/shehui/">社会</a></li>-->
     <li><a href="http://data.163.com/special/datablog/">数读</a></li>
     <li class="menu_war"><a href="http://war.163.com/">军事</a></li>
     <li class="menu_hangkong"><a href="http://news.163.com/air/">航空</a></li>
     <li class="menu_wurenji"><a href="http://news.163.com/uav/">无人机</a></li>
     <li><a href="http://news.163.com/college">新闻学院</a></li>
     <li><a href="http://gov.163.com/">政务</a></li>
     <li><a href="http://gongyi.163.com/">公益</a></li>
     <li><a href="http://media.163.com/">媒体</a></li>
     <li class="last"><a href="http://news.163.com/special/wangsansanhome/">王三三</a></li>
 </ul>
                        </div>
                    </div>
                </div>
                <!-- 头部导航 结束-->
                <!-- 内容区域 开始 -->
                <div class="ns_area clearfix index_main">
                    <!-- 新首左侧原创auditStart -->
                    <div class="main_origina_column" id="js_origina_column">
                        <div ne-module="/news/index2016_rmd/modules/originacolumn/originacolumn.js">
<div class="origina_column_warp">
	<h2>
		<span>新闻各有态度</span>
	</h2>
    <div class="scroll_bd" ne-role="scroll_bd">
        <div class="scroll_column_bd">
            <ul class="scroll_ul">
                <!-- 回声 开始 -->
            
                <!-- 回声 结束 -->
                <!-- 数读 开始 -->
                <li class="cell cell_sd cell_hover">
                    <p class="tag_line">
                        <a href="http://data.163.com/special/datablog/" class="tags tag_sd">数读</a>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://data.163.com/20/0717/20/FHP08AB1000181IU.html" class="detail" ne-role="detail">
                            <h3>
                                从虎扑女神大赛看，直男审美如何
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/3f17be23j00qdm5gk00atc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="从虎扑女神大赛看，直男审美如何">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://data.163.com/20/0713/14/FHE3R5UN00019GOE.html">山西女孩可爱第一名，吃醋第二名</a></li>
                                                        <li class="twoli "><a href="http://data.163.com/20/0712/22/FHC9QSVC000181IU.html">中国最爱下雨的地方是哪里</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 数读 结束 -->
                <!-- 人间 开始 -->
                <li class="cell cell_rj">
                    <p class="tag_line">
                        <a href="http://renjian.163.com/" class="tags tag_rj">人间</a>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://renjian.163.com/20/0717/10/FHNT47LF000181RV.html" class="detail" ne-role="detail">
                            <h3>
                                一进看守所，他就“精神病”了
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/845e9b12j00qdle0k001cc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="一进看守所，他就“精神病”了">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://renjian.163.com/20/0714/11/FHG9I2FT000181RV.html">被人言说散的换肾夫妻</a></li>
                                                        <li class="twoli "><a href="http://renjian.163.com/20/0709/16/FH40K5UP000181RV.html">人间这场局，谁能置身事外</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 人间 结束 -->
                <!-- 大国小民 开始 -->
                <li class="cell cell_dgxm">
                    <p class="tag_line">
                        <span class="tags tag_dgxm">大国小民</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://renjian.163.com/20/0715/10/FHIOM7VT000181RK.html" class="detail" ne-role="detail">
                            <h3>
                                为女相亲，小夏的人民公园历险记
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/fc1f0ea6j00qdhp25001oc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="为女相亲，小夏的人民公园历险记">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://renjian.163.com/20/0714/17/FHGTCP1P000181RK.html">在温哥华倒腾房子，我越买越穷</a></li>
                                                        <li class="twoli "><a href="http://renjian.163.com/20/0713/10/FHDKK2C0000181RK.html">工地上，那个被歧视的新手白领</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 大国小民 结束 -->
                <!-- 三三有梗 开始 -->
                <!-- 三三有梗 结束 -->
                <!-- 三三映画 开始 -->
                <!-- 三三映画 结束 -->
                <!-- 我去1990 开始 -->
                <!-- 我去1990 结束 -->
                <!-- 轻松一刻 开始 -->
                <li class="cell cell_qsyk">
                    <p class="tag_line">
                        <span class="tags tag_qsyk">轻松一刻</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="https://news.163.com/20/0717/18/FHONVAP7000181BR.html" class="detail" ne-role="detail">
                            <h3>
                                小心！你的手机里可能有个“窃贼”
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/1d17eb76j00qdlzxa000pc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="小心！你的手机里可能有个“窃贼”">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="https://news.163.com/20/0716/19/FHMAKRIT000181BR.html">"童养媳"都知道,"童养夫"还是头次听说</a></li>
                                                        <li class="twoli "><a href="https://news.163.com/20/0714/19/FHH63Q22000181BR.html">迷惑!SPA店诱惑顾客充值,却提供正规服务</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 轻松一刻 结束 -->
                <!-- 槽值 开始 -->
                <li class="cell cell_caozhi">
                    <p class="tag_line">
                        <span class="tags tag_caozhi">槽值</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://caozhi.news.163.com/20/0715/18/FHJJDKJB000181TI.html" class="detail" ne-role="detail">
                            <h3>
                                韩寒怎么就走到了这一步
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/6b6360dcj00qdi9tx003tc000go005kc.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="韩寒怎么就走到了这一步">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://caozhi.news.163.com/20/0714/18/FHH120V1000181TI.html">那些藏起胸部的中国女孩</a></li>
                                                        <li class="twoli "><a href="http://caozhi.news.163.com/20/0713/15/FHE4FOBC000181TI.html">500块一瓶的眼霜，没有平价替代</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 槽值 结束 -->
                <!-- 谈心社 开始 -->
                <li class="cell cell_tanxinshe">
                    <p class="tag_line">
                        <span class="tags tag_tanxinshe">谈心社</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="https://news.163.com/20/0716/13/FHLM15JA0001982T.html" class="detail" ne-role="detail">
                            <h3>
                                德云社的“门面担当”，凭什么是他？
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0716/26614933j00qdjrkd002jc000go005kc.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="德云社的“门面担当”，凭什么是他？">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="https://news.163.com/20/0716/15/FHLSK89L0001982T.html">16岁天才少女爆红，谁在制造神童</a></li>
                                                        <li class="twoli "><a href="https://news.163.com/20/0715/15/FHJB0TGM0001982T.html">40岁的陈冠希，你怎么老成这样了？</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 谈心社 结束 -->
                <!-- 看客 开始 -->
                <li class="cell cell_kanke">
                    <p class="tag_line">
                        <a href="http://renjian.163.com/special/renjian_kanke/" class="tags tag_kanke">看客</a>
                    </p>
                    <div class="column_main">
                                                                                                                                                                                         <a href="http://renjian.163.com/20/0716/09/FHL99JGS000199ET.html" class="detail" ne-role="detail">
                            <h3>
                                毕业后，我在新媒体公司卖性药
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0716/920ffc37p00qdjm01002qc0009c005uc.png?imageView&thumbnail=200y90" width="200" height="90" alt="毕业后，我在新媒体公司卖性药">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://renjian.163.com/20/0714/10/FHG6B13P000199ET.html">麻风病人被隔离的半个世纪</a></li>
                                                        <li class="twoli "><a href="http://renjian.163.com/20/0713/10/FHDKBVHA000199ET.html">暴富梦碎后，他们原地卖起了房</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 看客 结束 -->
                <!-- 身体密码 开始 -->
                <li class="cell cell_stpwd">
                    <p class="tag_line">
                        <a href="http://jiankang.163.com/special/zhutierji/?type=3" class="tags tag_stpwd">身体密码</a>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="https://jiankang.163.com/20/0706/17/FGSD8J9A00388AD5.html" class="detail" ne-role="detail">
                            <h3>
                                每年疼哭300万人的病 终于有疫苗了！
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0707/abc0f48bj00qd2wmt0008c0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="每年疼哭300万人的病 终于有疫苗了！">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="https://jiankang.163.com/20/0623/18/FFR0JAOA00388AD5.html">男生玩阿鲁巴是一种怎样的体验</a></li>
                                                        <li class="twoli "><a href="https://jiankang.163.com/20/0604/09/FE94EET40038804G.html">科学化解"人生之气"带来的尴尬</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 身体密码 结束 -->
                <!-- 哒哒 开始 -->
            
                <!-- 哒哒 结束 -->
            </ul>
        </div>
        <div id="js_baseline"></div>
        <span class="white_bg" id="js_white_bg"></span>
    </div>
</div>
</div>
                    </div>
                    <!-- 新首左侧原创auditEnd -->
                    <!-- 中间新闻 开始 -->
                    <div class="main_center_news">
                        <!-- 新首要闻auditStart -->
                        <div class="mod_top_news2 hidden">
                            <h2>
    <a href="https://news.163.com/20/0528/22/FDODVUHJ000189FH.html">十三届全国人大三次会议在京闭幕</a>
</h2>
<ul class="top_news_ul">
            <li><a href="https://news.163.com/20/0529/09/FDPMF599000189FH.html"><em class='fB cms-I_Blank_'>习近平给出中国经济发展之“策”</em></a> <a target="_blank" href="https://news.163.com/20/0529/09/FDPMCJIK000189FH.html"><em class='fB cms-I_Blank_'>一问:何为人民至上？</em></a></li>
        <li><a href="https://news.163.com/20/0530/03/FDRII1G80001899O.html">特朗普将取消给予香港的特别待遇政策豁免</a>|<a target="_blank" href="https://news.163.com/20/0530/02/FDRF0H8F0001899O.html">驻欧盟使团回应涉港声明</a></li>
        <li><a href="https://news.163.com/20/0530/04/FDRNDVFV0001899O.html">中国新技术试验卫星G星H星发射成功</a>|<a target="_blank" href="https://news.163.com/20/0530/02/FDRH19RQ0001899O.html">外交部回应韩美向"萨德"运设备</a></li>
    </ul>
<h2 class="top_news_title">
    <a href="https://news.163.com/20/0602/23/FE5EE92D000189FH.html">习近平：把人民的生命和健康放在第一位</a>
</h2>
<ul class="top_news_ul">
            <li><a href="https://news.163.com/20/0530/00/FDR93ABN0001899O.html">推特市值蒸发135亿后"硬刚"特朗普</a>|<a target="_blank" href="https://news.163.com/20/0530/02/FDRE649B0001899O.html">加拿大医生感染新冠后继续工作</a></li>
        <li><a href=" https://news.163.com/20/0530/01/FDRAMOLJ0001899O.html">南非失业率恐飙升至50%以上</a>|<a target="_blank" href="https://news.163.com/20/0530/02/FDRDUK010001899O.html">英政府"强制休假"计划十月底将结束</a></li>
        <li><a href="https://news.163.com/20/0530/01/FDRBTJ6S0001899O.html">隧洞垮塌3名工人被埋7天 靠洞内积水生还</a>|<a target="_blank" href="https://news.163.com/20/0530/01/FDRAGM8H0001899O.html">副市长的车闯红灯被曝光</a></li>
    </ul>
                        </div>
                        <div class="mod_top_news2" id="js_top_news">
                            <!-- 北京新闻 -->
                            <div class="news_bj_news" ne-class="{{myState.topnews ? 'news_news_show': 'news_news_hide'}}">
                                                                                                                                                                                    <h2>
                                            <a href="https://news.163.com/20/0718/12/FHQM7V6T000189FH.html">人民至上、生命至上，习近平这样部署防汛救灾 </a>
                                        </h2>
                                                                                                                                                                                                                                    <ul class="top_news_ul">
                                                <li><a href="https://news.163.com/20/0718/12/FHQMAK67000189FH.html"><em class='fB cms-I_Blank_'>习近平：切实做好防汛救灾</em></a> <a target="_blank" href="https://news.163.com/20/0718/12/FHQMD08Q000189FH.html"><em class='fB cms-I_Blank_'>从最字读懂中国共产党领导</em></a></li>
                                                                                                                                                                                                                                    <li><a href="http://dy.163.com/article/FHO8JJFK0514R9OJ.html">专家评美方签署所谓“香港自治法案”</a> <a target="_blank" href="https://dy.163.com/article/FHP0E1PO05346RC6.html">香港青年周文港</a></li>
                                                                                                                                                                                                                                    <li><a href="http://dy.163.com/article/FHQ1EFCM0514R9M0.html">“西藏各方面发展成就全世界有目共睹”</a></li>
                                                                                                                                                                                                                                    <li><a href="http://dy.163.com/article/FHPETFRA053469KC.html">外交部新任发言人是他 昔日同窗回忆：极具口才</a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/08/FHQA8GA30001899O.html"><em class='fB cms-I_Blank_'>卫健委:昨日新增确诊病例22例 本土16例均在新疆</em></a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/02/FHPKC49H0001899O.html">莫斯科市市长：60%的莫斯科市民已获得群体免疫</a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/02/FHPKK7JD0001899O.html">英军称要派出庞大航母编队来南海 英网民评论亮了</a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/11/FHQJHHHM0001899O.html">乌鲁木齐全市正做核酸检测 12日半夜就有人被隔离</a></li>
                                                                                                                                                                                                                                    </ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                            </div>
                            <!-- 全国新闻 -->
                            <div class="news_default_news" ne-class="{{!myState.topnews ? 'news_news_show': 'news_news_hide'}}">
                                                                                                                                                                                    <h2>
                                            <a href="https://news.163.com/20/0718/12/FHQM7V6T000189FH.html">人民至上、生命至上，习近平这样部署防汛救灾 </a>
                                        </h2>
                                                                                                                                                                                                                                    <ul class="top_news_ul">
                                                <li><a href="https://news.163.com/20/0718/12/FHQMAK67000189FH.html"><em class='fB cms-I_Blank_'>习近平：切实做好防汛救灾</em></a> <a target="_blank" href="https://news.163.com/20/0718/12/FHQMD08Q000189FH.html"><em class='fB cms-I_Blank_'>从最字读懂中国共产党领导</em></a></li>
                                                                                                                                                                                                                                    <li><a href="http://dy.163.com/article/FHO8JJFK0514R9OJ.html">专家评美方签署所谓“香港自治法案”</a> <a target="_blank" href="https://dy.163.com/article/FHP0E1PO05346RC6.html">香港青年周文港</a></li>
                                                                                                                                                                                                                                    <li><a href="http://dy.163.com/article/FHQ1EFCM0514R9M0.html">“西藏各方面发展成就全世界有目共睹”</a></li>
                                                                                                                                                                                                                                    <li><a href="http://dy.163.com/article/FHPETFRA053469KC.html">外交部新任发言人是他 昔日同窗回忆：极具口才</a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/08/FHQA8GA30001899O.html"><em class='fB cms-I_Blank_'>卫健委:昨日新增确诊病例22例 本土16例均在新疆</em></a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/02/FHPKC49H0001899O.html">莫斯科市市长：60%的莫斯科市民已获得群体免疫</a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/02/FHPKK7JD0001899O.html">英军称要派出庞大航母编队来南海 英网民评论亮了</a></li>
                                                                                                                                                                                                                                    <li><a href="https://news.163.com/20/0718/11/FHQJHHHM0001899O.html">乌鲁木齐全市正做核酸检测 12日半夜就有人被隔离</a></li>
                                                                                                                                                                                                                                    </ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                            </div>
                        </div>
                        <!-- 新首要闻auditEnd -->
                        <!-- 广告 开始 -->
                        <div class="mod_top_news_ad">
                            <!-- 16新闻首页01小通栏 -->
<a href="http://gb.corp.163.com/gb/legal.html" class="ad_hover_href"></a>
<!-- 广告位：网易-新闻频道-首页-01小通栏 -->
<div id="ssp_6904941"></div>
<script>
(function() {
    (window.slotbydup=window.slotbydup || []).push({
        id: '6904941',
        container: 'ssp_6904941',
        size: '600,50',
        display: 'inlay-fix',
        async: true
    });
})();
</script>
                        </div>
                        <!-- 广告 结束 -->
                        <!-- 特别报道 开始 -->
                        <!--<div class="mod_important_news none">
    <h5><label>特别报道</label></h5>
            <h2>
        <a href="http://news.163.com/16/0721/19/BSH7V8QF00014JB6.html">辽宁遭暴雨侵袭致城市内涝 紧急转移12万人</a>
    </h2>
        <ul class="top_news_ul">
                        <li><a href="http://news.163.com/16/0721/10/BSG7HOH20001124J.html">民政部:北方暴雨75人死亡失踪</a>|<a target="_blank" href="http://news.163.com/16/0721/12/BSGG5VK300011229.html">北京发生山洪灾害 铲车翻倒4人被困</a></li>
                <li><a href="http://news.163.com/16/0721/12/BSGHHVLK00011229.html">搜救犬水灾救援22天殉职 主人:它太累了</a>|<a target="_blank" href="http://news.163.com/16/0721/07/BSFUFFP800014AED.html">姐妹被洪水卷走警方拒立案</a></li>
            </ul>
    <div class="mod_important_pic">
        <ul class="clearfix">
                                    <li>
                <a href="http://news.163.com/photoview/00AN0001/2189402.html?from=ph_ss#p=BSG716GE00AN0001">
                    <img ne-lazy="effect: fadeIn;tabIndex:0" data-original="http://img3.cache.netease.com/news/2016/7/21/20160721131401d35e2.jpg" width="190" height="120"/>
                    <span class="bg"></span>
                    <h3>河南遇强降雨 9.8万人转移</h3>
                </a>
            </li>
                        <li>
                <a href="http://news.163.com/photoview/00AP0001/2189377.html?from=ph_ss#p=BSFTQ99H00AP0001">
                    <img ne-lazy="effect: fadeIn;tabIndex:0" data-original="http://img3.cache.netease.com/news/2016/7/21/201607211319466e84e.jpg" width="190" height="120"/>
                    <span class="bg"></span>
                    <h3>女主播直播暴雨 浑身湿透</h3>
                </a>
            </li>
                        <li>
                <a href="http://news.163.com/photoview/00AP0001/2189389.html?from=ph_ss#p=BSG1S9AM00AP0001">
                    <img ne-lazy="effect: fadeIn;tabIndex:0" data-original="http://img5.cache.netease.com/news/2016/7/21/20160721132119ef59b.jpg" width="190" height="120"/>
                    <span class="bg"></span>
                    <h3>湖北民众省道上趟水摸鱼</h3>
                </a>
            </li>
                    </ul>
    </div>                  
</div>-->
                        <!-- 特别报道 结束 -->
                        <!-- 网易公开课 开始-->
                        <div ne-module="/news/index2016_rmd/modules/slide/slide.js" class="mod_netes_origina">
<script type="text/javascript" _keep="true">
    window.GGKSLIDEDATA = [
                                                                         {
            "title":"如果建造一座10亿层的摩天大楼，会怎样？",
            "imgsrc":"https://cms-bucket.ws.126.net/2020/0716/0cf44950j00qdjs3g002kc000go006yc.jpg?imageView&thumbnail=600y250",
            "link":"http://open.163.com/newview/movie/courseintro?newurl=WEDQ626LA#share-mob"
        }
                                                         ,
                {
            "title":"麦家：原生家庭欠你的，你总要自己拿回来",
            "imgsrc":"https://cms-bucket.ws.126.net/2020/0716/7f659baaj00qdjqew000cc000go006yc.jpg?imageView&thumbnail=600y250",
            "link":"http://open.163.com/newview/movie/courseintro?newurl=FEBVEER5U#share-mob"
        }
                                                         ,
                {
            "title":"帅哥美女带你备考雅思托福",
            "imgsrc":"https://cms-bucket.ws.126.net/2020/0714/eff52505j00qdfxze000ec000go006yc.jpg?imageView&thumbnail=600y250",
            "link":"http://open.163.com/newview/movie/courseintro?newurl=ME1GH6IJE#share-mob"
        }
                                                         ,
                {
            "title":"爱情和欲望的6个不同之处",
            "imgsrc":"https://cms-bucket.ws.126.net/2020/0714/2f91518cj00qdfxvx000jc000go006yc.jpg?imageView&thumbnail=600y250",
            "link":"http://open.163.com/newview/movie/courseintro?newurl=MEFB9UUOH#share-mob"
        }
            ];
</script>
<div ne-module="/modules/slide/slide.js" class="mod_idx_focus" ne-props="events:mouseover;interval:4000;topicid=000501EP;listnum=8;pointstart=80;pointend=100;" ne-state="slideMethod:left;events=mouseover;interval=4000">
    <div class="hd">
        <h2><a href="https://open.163.com/">网易公开课</a></h2>
        <div class="focus_ctrl">
            <span ne-role="slide-nav"></span>
            <span ne-role="slide-nav"></span>
            <span ne-role="slide-nav"></span>
            <span ne-role="slide-nav"></span>
        </div>
    </div>
    <a ne-role="slide-prev" class="focus_prev"></a>
    <a ne-role="slide-next" class="focus_next"></a>
    
    <div ne-role="slide-body" class="focus_body">
        <ul ne-role="slide-scroll">
            <script type="text/template" ne-foreach="gkkdatalist">
            <li <%if(__i == 0){%>class="current"<%}%> ne-role="slide-page">
                <a href="<%=link%>" title="<%=title%>" class="photo"><img src="<%=imgsrc%>" width="600" height="250" alt="<%=title%>"/></a>
                <span class="bg"></span>
                <h3>
                    <a href="<%=link%>"><%=title%></a>
                </h3>
            </li>
            </script>
        </ul>
        <span class="ad_hover_pic">广告</span>
    </div>
</div>
</div>
                        <!-- 网易公开课 结束-->
                        <!-- 信息流 开始-->
                        <div ne-module="/news/index2016_rmd/modules/datalist2016/datalist2016.js" ne-extend="/news/index2016_rmd/modules/datalist2016/config.js" class="mod_datalist" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
<!-- 新闻本地索引配置 -->
<script type="text/javascript" _keep="true">
var  newsProvinceData = {
    "北京市": {
	    "inc": "https://house.163.com/special/00078GU7/beijign_xw_news_v1.js",
            "url": "http://bj.news.163.com/"
	},
        "天津市": {
	    "inc": "https://house.163.com/special/00078GU7/tianjin2_xw_news_v1.js",
            "url": "http://news.163.com/"
	},
	"上海市": {
	    "inc": "https://house.163.com/special/00078GU7/shanghai2_xw_news_v1.js",
            "url": "http://sh.news.163.com/"
	},
        "重庆市": {
	    "inc": "https://house.163.com/special/00078GU7/chongqing2_xw_news_v1.js",
            "url": "http://chongqing.163.com/"
	}
        ,"日本":{
            "inc":"https://house.163.com/special/00078GU8/japan_xw_news_v1.js",
            "url": ""
    }
        ,"福建省":{
            "inc":"https://house.163.com/special/00078GU8/fujian2_xw_news_v1.js",
            "url": "http://fj.news.163.com"
    }
        ,"安徽省":{
            "inc":"https://house.163.com/special/00078GU8/anhui2_xw_news_v1.js",
            "url": "http://ah.news.163.com"
    }
        ,"西藏自治区":{
            "inc":"https://house.163.com/special/00078GU8/tibet_xw_news_v1.js",
            "url": "http://news.163.com/"
    }
        ,"浙江省":{
            "inc":"https://house.163.com/special/00078GU8/zhejiang_xw_news_v1.js",
            "url": "http://news.163.com/"
    }
        ,"云南省":{
            "inc":"https://house.163.com/special/00078GU8/yunnan_xw_news_v1.js",
            "url": "http://yn.news.163.com/"
    }
        ,"新疆维吾尔自治区":{
            "inc":"https://house.163.com/special/00078GU8/xinjiang_xw_news_v1.js",
            "url": "http://xj.news.163.com/"
    }
        ,"四川省":{
            "inc":"https://house.163.com/special/00078GU8/sichuan_xw_news_v1.js",
            "url": "http://news.163.com/"
    }
        ,"陕西省":{
            "inc":"https://house.163.com/special/00078GU8/shaanxi_xw_news_v1.js",
            "url": "http://shanxi.news.163.com/"
    }
        ,"山西省":{
            "inc":"https://house.163.com/special/00078GU8/shanxi_xw_news_v1.js",
            "url": "http://news.163.com/"
    }
        ,"山东省":{
            "inc":"https://house.163.com/special/00078GU8/shandong_xw_news_v1.js",
            "url": "http://sd.news.163.com/"
    }
        ,"青海省":{
            "inc":"https://house.163.com/special/00078GU8/qinghai_xw_news_v1.js",
            "url": "http://news.163.com"
    }
        ,"宁夏回族自治区":{
            "inc":"https://house.163.com/special/00078GU8/ningxia_xw_news_v1.js",
            "url": "http://ningxia.news.163.com/"
    }
        ,"内蒙古自治区":{
            "inc":"https://house.163.com/special/00078GU8/inner_xw_news_v1.js",
            "url": "http://hhht.news.163.com/"
    }
        ,"辽宁省":{
            "inc":"https://house.163.com/special/00078GU8/liaoning_xw_news_v1.js",
            "url": "http://liaoning.news.163.com/"
    }
        ,"江西省":{
            "inc":"https://house.163.com/special/00078GU8/jiangxi_xw_news_v1.js",
            "url": "http://jx.news.163.com/"
    }
        ,"江苏省":{
            "inc":"https://house.163.com/special/00078GU8/jiangsu_xw_news_v1.js",
            "url": "http://js.news.163.com/"
    }
        ,"吉林省":{
            "inc":"https://house.163.com/special/00078GU8/jilin_xw_news_v1.js",
            "url": "http://jl.news.163.com/"
    }
        ,"湖南省":{
            "inc":"https://house.163.com/special/00078GU8/hunan_xw_news_v1.js",
            "url": "http://hunan.news.163.com/"
    }
        ,"湖北省":{
            "inc":"https://house.163.com/special/00078GU8/hubei_xw_news_v1.js",
            "url": "http://hb.news.163.com/"
    }
        ,"黑龙江省":{
            "inc":"https://house.163.com/special/00078GU8/longjiang_xw_news_v1.js",
            "url": "http://hlj.news.163.com/"
    }
        ,"河南省":{
            "inc":"https://house.163.com/special/00078GU8/henan_xw_news_v1.js",
            "url": "http://henan.163.com/"
    }
        ,"河北省":{
            "inc":"https://house.163.com/special/00078GU8/hebei_xw_news_v1.js",
            "url": "http://hebei.news.163.com/"
    }
        ,"海南省":{
            "inc":"https://house.163.com/special/00078GU8/hainan_xw_news_v1.js",
            "url": "http://hn.news.163.com/"
    }
        ,"贵州省":{
            "inc":"https://house.163.com/special/00078GU8/guizhou_xw_news_v1.js",
            "url": "http://gz.news.163.com/"
    }
        ,"广西壮族自治区":{
            "inc":"https://house.163.com/special/00078GU8/guangxi_xw_news_v1.js",
            "url": "http://gx.news.163.com/"
    }
        ,"广东省":{
            "inc":"https://house.163.com/special/00078GU8/guangdong_xw_news_v1.js",
            "url": "http://gd.news.163.com"
    }
        ,"甘肃省":{
            "inc":"https://house.163.com/special/00078GU8/gansu_xw_news_v1.js",
            "url": "http://gs.news.163.com/"
    }
        ,"beijingapi" : "https://house.163.com/special/00078GU7/beijign_xw_news_v1.js"
};
</script>
<div class="newsdata_wrap" ne-on="showed:changepanel" ne-module="/modules/tabs/tabs.js" ne-state="showhide:true;delay:400;">
    <div class="newsdata_nav" ne-class="{{myState.fixedTop ? 'fixed_top':''}}">
        <ul class="clearfix">
            <li class="nav_item">
                <a class="nav_name no_cursor" ne-role="tab-nav" href="javascript:;" target="_self">
                    要闻
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <li class="nav_item">
                <a class="nav_name no_cursor" ne-role="tab-nav" href="{{myState.channelbendiurl}}" target="{{myState.channelbendiurl == 'javascript:;' ? '_self' : '_blank'}}" ne-class="{{myState.bendiTstyle ? 'bendistyle' : ''}}">
                    <strong ne-text="{{myState.bendiCity}}"></strong>
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <!-- <li class="nav_item">
                <a class="nav_name" ne-role="tab-nav" href="http://news.163.com/shehui/">
                    社会
                    <span class="nav_item_ink"></span>
                </a>
            </li> -->
            <li class="nav_item">
                <a class="nav_name" ne-role="tab-nav" href="http://news.163.com/domestic/">
                    国内
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <li class="nav_item">
                <a class="nav_name" ne-role="tab-nav" href="http://news.163.com/world/">
                    国际
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <li class="nav_item">
                <a class="nav_name no_cursor" ne-role="tab-nav" href="javascript:;" target="_self">
                    独家
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <li class="nav_item">
                <a class="nav_name" ne-role="tab-nav" href="http://war.163.com/">
                    军事
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <li class="nav_item">
                <a class="nav_name" ne-role="tab-nav" href="http://money.163.com/">
                    财经
                    <span class="nav_item_ink"></span>
                </a>
            </li>
            <li class="nav_item">
                <a class="nav_name" ne-role="tab-nav" href="http://tech.163.com/">
                    科技
                    <span class="nav_item_ink"></span>
                </a>
            </li>
        </ul>
        <a class="more" href="javascript:;" ne-mouseover="moreShowChannel()" ne-mouseout="morehideChannel()" ne-role="morebtn" ne-class="{{myState.morechannel ? 'more_hover': ''}}" target="_self">更多</a>
        <div class="more_list" ne-click="moreList($event)" ne-show="{{myState.morechannel}}" ne-role="more_list">
            <!-- <a ne-role="tab-nav" href="http://tech.163.com/">科技</a> -->
            <a ne-role="tab-nav" href="http://sports.163.com/">体育</a>
            <a ne-role="tab-nav" href="http://ent.163.com/">娱乐</a>
            <a ne-role="tab-nav" href="http://lady.163.com/">时尚</a>
            <a ne-role="tab-nav" href="http://auto.163.com/">汽车</a>
            <a ne-role="tab-nav" href="{{myState.channelhouseurl}}">房产</a>
            <a ne-role="tab-nav" href="http://news.163.com/air/">航空</a>
            <a ne-role="tab-nav" href="http://jiankang.163.com/">健康</a>
        </div>
    </div>
    <a href="#prev" ne-click="tabPrevFn($event);" class="newsdata_prev"  ne-class="{{myState.fixedTop ? 'fixed_data_show': ''}}" ne-hide="{{myState.iPad}}">
        <span></span>
        <div class="newsdata_btn_name">{{myState.preBtnName}}</div>
    </a>
   
    <a href="#next" ne-click="tabNextFn($event);" class="newsdata_next" ne-class="{{myState.fixedTop ? 'fixed_data_show': ''}}" ne-hide="{{myState.iPad}}">
        <span></span>
        <div class="newsdata_btn_name">{{myState.nextBtnName}}</div>
    </a>
    <ul class="newsdata_list" ne-class="{{myState.fixedTop ? 'fixed_bar_padding': ''}} {{myState.bgLoading ? 'bgloading': 'noloading'}}">
        <li class="newsdata_item" ne-role="tab-body" ne-repeat="body in navList">
            <div class="ndi_main" ne-class="{{myState.message > 0 ? 'show_message':''}}">
                <script type="text/template" ne-repeat="newrow in datalist[__i]">
                <%if(newrow.style == "iframe"){%>
                    <div class="at_item info_ad_item news_iframe_ad" adType="infoAd" ne-click="adClickTracker(<%=newrow.infoAdIdx%>,'infoAd')">
                        <iframe src="<%=newrow.iframe[0].link%>" width="<%=newrow.iframe[0].iframewidth || 600 %>" height="<%=newrow.iframe[0].iframeheight || 100 %>" frameborder="0" border="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>
                    </div>
                <%}else if(newrow.style == "docAD"){%>
                    <div class="at_item info_ad_item news_article clearfix" adType="infoAd" ne-click="adClickTracker(<%=newrow.infoAdIdx%>,'infoAd')">
                        <a href="<%=newrow.relatedActionLinks[0].url%>" class="na_pic">
                            <img src="<%=newrow.resources[0].urls[0]%>" width="140" height="88">
                        </a>
                        <div class="na_detail clearfix">
                            <div class="news_title">
                                <h3><strong><a href="<%=newrow.relatedActionLinks[0].url%>"><%=newrow.title%></a>
                                </strong></h3>
                            </div>
                        </div>
                        <div class="ad_detail clearfix">
                            <span class="tg_tag"><%=newrow.source%></span>
                            <span class="keywords" ne-html="<%=newrow.content%>"></span>
                        </div>
                    </div>
                <%} else if(newrow.style == "photosetAD"){%>
                    <div class="at_item info_ad_item news_photoview clearfix news_ad_photoview" adType="infoAd" ne-click="adClickTracker(<%=newrow.infoAdIdx%>,'infoAd')">
                        <div class="news_title">
                            <h3><strong><a href="<%=newrow.relatedActionLinks[0].url%>"><%=newrow.title%></a></strong></h3>
                        </div>
                        <div class="np_pic">
                            <a href="<%=newrow.relatedActionLinks[0].url%>">
                                <span class="p_img3">
                                    <img src="<%=newrow.resources[0].urls[0]%>" width="190" height="120">
                                </span>
                                <span class="p_img3">
                                    <img src="<%=newrow.resources[0].urls[1]%>" width="190" height="120">
                                </span>
                                <span class="p_img3">
                                    <img src="<%=newrow.resources[0].urls[2]%>" width="190" height="120" class="pic_last">
                                </span>
                            </a>
                        </div>
                        <div class="ad_detail clearfix">
                            <span class="tg_tag"><%=newrow.source%></span>
                            <span class="keywords" ne-html="<%=newrow.content%>"></span>
                        </div>
                    </div>
                <%} else if(newrow.style == "columsAD"){%>
                    <div class="at_item info_ad_item news_special clearfix news_ad_special" adType="infoAd" ne-click="adClickTracker(<%=newrow.infoAdIdx%>,'infoAd')">
                        <div class="news_title">
                            <h3><strong><a href="<%=newrow.relatedActionLinks[0].url%>"><%=newrow.title%></a></strong></h3>
                        </div>
                        <a href="<%=newrow.relatedActionLinks[0].url%>" class="ns_pic"><img src="<%=newrow.resources[0].urls[0]%>" width="600" height="200"></a>
                        <div class="ad_detail clearfix">
                            <span class="tg_tag"><%=newrow.source%></span>
                            <span class="keywords" ne-html="<%=newrow.content%>"></span>
                        </div>
                    </div>
                <%} else if(newrow.imgurl && newrow.add1 && newrow.add2 && /\.jpg$|\.png$|\.jpeg$|\.gif$/.test(newrow.imgurl) && /\.jpg$|\.png$|\.jpeg$|\.gif$/.test(newrow.add1) && /\.jpg$|\.png$|\.jpeg$|\.gif$/.test(newrow.add2)){%>
                    <div class="data_row news_photoview clearfix <%if(__i == 0){%>news_first <%}%>">
                        <div class="news_title">
                            <h3><a href="<%=newrow.docurl%>"><%=newrow.title%></a></h3>
                        </div>
                        <div class="np_pic">
                            <a href="<%=newrow.docurl%>">
                                <span class="p_img3">
                                <%if(newrow.imgurl.indexOf('gif') != -1){%>
                                <img src="<%=newrow.imgurl%>" width="190" height="120" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/pic3_error0106.jpg';">
                                <%} else {%> 
                                <img src="<%=newrow.imgurl%>?imageView&thumbnail=190y120&quality=85" width="190" height="120" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/pic3_error0106.jpg';">
                                <%}%> 
                                </span>
                                <span class="p_img3">
                                <%if(newrow.add1.indexOf('gif') != -1){%>
                                <img src="<%=newrow.add1%>" width="190" height="120" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/pic3_error0106.jpg';">
                                <%} else {%> 
                                <img src="<%=newrow.add1%>?imageView&thumbnail=190y120&quality=85" width="190" height="120" onerror="javascript:this.src='https://static.ws.126.net/f2e/index2016_rmd/images/pic3_error0106.jpg';">
                                <%}%> 
                                </span>
                                <span class="p_img3">
                                <%if(newrow.add2.indexOf('gif') != -1){%>
                                <img src="<%=newrow.add2%>" width="190" height="120" class="pic_last" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/pic3_error0106.jpg';">
                                <%} else {%> 
                                <img src="<%=newrow.add2%>?imageView&thumbnail=190y120&quality=85" width="190" height="120" class="pic_last" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/pic3_error0106.jpg';">
                                <%}%> 
                                </span>
                            </a>
                        </div>
                        <div class="np_detail clearfix">
                            <div class="news_tag">
                                <%if(newrow.channelname && newrow.channelname != "shehui" && newrow.channelname != "guonei" && newrow.channelname != "guoji" && newrow.channelname != "dada" && newrow.channelname != "war" && newrow.channelname != "hangkong"){%>
                                    <%if(newrow.tlastid != ""){%>
                                        <strong class="barlink"><%=newrow.tlastid%></strong>
                                    <%}else if(newrow.label != ""){%>
                                        <a href="<%=newrow.tlink%>" class="link link_more">
                                        <em><%=newrow.label%></em></a>
                                    <%}%> 
                                <%}%>
                                <%if(newrow.keywords.length > 0){%>
                                    <div class="keywords">
                                    <%if(newrow.newstype == "photoset"){%>
                                        <%bowlder.each(newrow.keywords,function(k){%>
                                            <a href="javascript:;" target="_self" style="cursor:default;"><%=k.keyname%></a>
                                        <%})%> 
                                    <%}else{%>
                                        <%bowlder.each(newrow.keywords,function(k){%>
                                            <a href="<%=k.akey_link%>"><%=k.keyname%></a>
                                        <%})%> 
                                    <%}%>
                                    </div>
                                <%}%> 
                                <%if(newrow.time){%>
                                    <span class="time"><%=formatTime(newrow.time)%></span>
                                <%}%> 
                            </div>
                            <div class="share-join clearfix">
                                <%if(newrow.tienum != ""){%>
                                <a class="post_recommend_tie right" href="<%=newrow.commenturl%>" >
                                    <div class="post_recommend_tie_wrap">
                                        <span class="post_recommend_tie_icon icons"><%=newrow.tienum%></span> 
                                        <span class="post_recommend_tie_text"><i>跟贴</i><%=newrow.tienum%></span>
                                    </div>
                                </a>
                                <%}%>
                                <div class="ne-shares-parent right">
                                    <span href="#share" title="分享" class="ne-shares-arr"></span>
                                    <div class="share-join-item" ne-module="/modules/shares/shares.js" ne-state="cls.hover:ne-shares-open;title:<%=newrow.title%>;url:<%=newrow.docurl%>;pic:<%=newrow.imgurl%>" >
<div class="ne-shares-pop6x1wrap" ne-role="share-wrap">
<ul class="ne-shares-pop6x1">
    <li>
        <a ne-click="share('yixin')" href="http://yixin.im/#f=www">
            <span class="inner">
                <i class="ep-share-icon ep-share-yixin"></i>
                <span class="ep-share-name">易信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-mouseover="initWeixin()" href="javascript:" target="_self" class="ne-shares-weixin">
            <span class="inner">
                <i class="ep-share-icon ep-share-weixin"></i>
                <span class="ep-share-name">微信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-click="share('sina')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-sina"></i>
                <span class="ep-share-name">微博</span>
            </span>
        </a>
    </li>
    <li class="last">
        <a ne-click="share('qzone')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-qzone"></i>
                <span class="ep-share-name">QQ空间</span>
            </span>
        </a>
    </li>
</ul>
</div>
<div class="ne-shares-qrwrap">
  <div class="ne-shares-qrarr"></div>
  <div ne-role="qrcode" class="ne-shares-qrcode"></div>
  <p>用微信扫码二维码</p><p>分享至好友和朋友圈</p>
</div>
</div>
                                </div>
                            </div>
                        </div>
                    </div>
                <%} else if(newrow.add1 && /\.jpg$|\.png$|\.jpeg$|\.gif$/.test(newrow.add1)){%>
                    <div class="data_row news_special clearfix <%if(__i == 0){%>news_first <%}%>">
                        <div class="news_title">
                            <h3><a href="<%=newrow.docurl%>"><%=newrow.title%></a></h3>
                            <%if(newrow.channelname && newrow.channelname != "shehui" && newrow.channelname != "guonei" && newrow.channelname != "guoji" && newrow.channelname != "dada" && newrow.channelname != "war" && newrow.channelname != "hangkong"){%>
                                <%if(newrow.tlastid != ""){%>
                                    <strong class="barlink"><%=newrow.tlastid%></strong>
                                <%}else if(newrow.label != ""){%>
                                    <a href="<%=newrow.tlink%>" class="link link_more">
                                    <em><%=newrow.label%></em></a>
                                <%}%> 
                            <%}%>
                        </div>
                        <a href="<%=newrow.docurl%>" class="ns_pic">
                            <%if(newrow.add1.indexOf('gif') != -1){%>
                            <img src="<%=newrow.add1%>" alt="<%=newrow.title%>" width="600" height="300" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/special_error0106.jpg';">
                            <%} else {%> 
                            <img src="<%=newrow.add1%>?imageView&thumbnail=600y300&quality=85" alt="<%=newrow.title%>" width="600" height="300" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/special_error0106.jpg';">
                            <%}%> 
                        </a>
                    </div>
                <%} else if(newrow.imgurl && newrow.imgurl != ""){%>
                    <div class="data_row news_article clearfix <%if(__i == 0){%>news_first<%}%>">
                        <%if(newrow.imgurl != ""){%>
                            <a href="<%=newrow.docurl%>" class="na_pic">
                                <%if(newrow.imgurl.indexOf('gif') != -1){%>
                                <img src="<%=newrow.imgurl%>" alt="<%=newrow.title%>" width="140" height="88" onerror="imgError(this)">
                                <%} else {%> 
                                <img src="<%=newrow.imgurl%>?imageView&thumbnail=140y88&quality=85" alt="<%=newrow.title%>" width="140" height="88" onerror="imgError(this)">
                                <%}%> 
                            </a>
                        <%}%> 
                        <div class="na_detail clearfix <%if(newrow.imgurl == ""){%>no_pic<%}%>">
                            <div class="news_title">
                                <h3><a href="<%=newrow.docurl%>"><%=newrow.title%></a></h3>
                            </div>
                            <div class="news_tag">
                                <%if(newrow.channelname && newrow.channelname != "shehui" && newrow.channelname != "guonei" && newrow.channelname != "guoji" && newrow.channelname != "dada" && newrow.channelname != "war" && newrow.channelname != "hangkong"){%>
                                    <%if(newrow.tlastid != ""){%>
                                        <strong class="barlink"><%=newrow.tlastid%></strong>
                                    <%}else if(newrow.label != ""){%>
                                        <a href="<%=newrow.tlink%>" class="link link_more">
                                        <em><%=newrow.label%></em></a>
                                    <%}%> 
                                <%}%>
                                <%if(newrow.keywords && newrow.keywords.length > 0){%>
                                    <div class="keywords">
                                    <%bowlder.each(newrow.keywords,function(k){%>
                                        <a href="<%=k.akey_link%>"><%=k.keyname%></a>
                                    <%})%> 
                                    </div>
                                <%}%> 
                                <%if(newrow.time){%>
                                    <span class="time"><%=formatTime(newrow.time)%></span>
                                <%}%> 
                            </div>
                            <div class="share-join clearfix">
                                <a class="post_recommend_tie right" href="<%=newrow.commenturl%>" >
                                    <div class="post_recommend_tie_wrap">
                                        <span class="post_recommend_tie_icon icons"><%=newrow.tienum ? newrow.tienum : 0%></span> 
                                        <span class="post_recommend_tie_text"><i>跟贴</i><%=newrow.tienum%></span>
                                    </div>
                                </a>
                                <div class="ne-shares-parent right">
                                    <span href="#share" title="分享" class="ne-shares-arr"></span>
                                    <div class="share-join-item" ne-module="/modules/shares/shares.js" ne-state="cls.hover:ne-shares-open;title:<%=newrow.title%>;url:<%=newrow.docurl%>;pic:<%=newrow.imgurl%>" >
<div class="ne-shares-pop6x1wrap" ne-role="share-wrap">
<ul class="ne-shares-pop6x1">
    <li>
        <a ne-click="share('yixin')" href="http://yixin.im/#f=www">
            <span class="inner">
                <i class="ep-share-icon ep-share-yixin"></i>
                <span class="ep-share-name">易信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-mouseover="initWeixin()" href="javascript:" target="_self" class="ne-shares-weixin">
            <span class="inner">
                <i class="ep-share-icon ep-share-weixin"></i>
                <span class="ep-share-name">微信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-click="share('sina')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-sina"></i>
                <span class="ep-share-name">微博</span>
            </span>
        </a>
    </li>
    <li class="last">
        <a ne-click="share('qzone')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-qzone"></i>
                <span class="ep-share-name">QQ空间</span>
            </span>
        </a>
    </li>
</ul>
</div>
<div class="ne-shares-qrwrap">
  <div class="ne-shares-qrarr"></div>
  <div ne-role="qrcode" class="ne-shares-qrcode"></div>
  <p>用微信扫码二维码</p><p>分享至好友和朋友圈</p>
</div>
</div>
                                </div>
                            </div>
                        </div>
                    </div>
                <%} else if(newrow.pics3 && newrow.pics3.length >= 3){%>
                    <div class="data_row news_photoview clearfix <%if(__i == 0){%>news_first <%}%>">
                        <div class="news_title">
                            <h3><a href="<%=newrow.docurl%>"><%=newrow.title%></a></h3>
                        </div>
                        <div class="np_pic">
                            <a href="<%=newrow.docurl%>">
                                <%bowlder.each(newrow.pics3,function(n){%>
                                    <span class="p_img3">
                                    <img src="<%=n.pic%>" width="190" height="120" onerror="javascript:this.src='https://static.ws.126.net/f2e/news/index2016_rmd/images/pic3_error0106.jpg';">
                                    </span>
                                <%})%> 
                            </a>
                        </div>
                        <div class="np_detail clearfix">
                            <div class="news_tag">
                                <%if(newrow.channelname && newrow.channelname != "shehui" && newrow.channelname != "guonei" && newrow.channelname != "guoji" && newrow.channelname != "dada" && newrow.channelname != "war" && newrow.channelname != "hangkong"){%>
                                    <%if(newrow.tlastid != ""){%>
                                        <strong class="barlink"><%=newrow.tlastid%></strong>
                                    <%}else if(newrow.label != ""){%>
                                        <a href="<%=newrow.tlink%>" class="link link_more">
                                        <em><%=newrow.label%></em></a>
                                    <%}%> 
                                <%}%>
                                <%if(newrow.keywords && newrow.keywords.length > 0){%>
                                    <div class="keywords">
                                    <%if(newrow.newstype == "photoset"){%>
                                        <%bowlder.each(newrow.keywords,function(k){%>
                                            <a href="javascript:;" target="_self" style="cursor:default;"><%=k.keyname%></a>
                                        <%})%> 
                                    <%}else{%>
                                        <%bowlder.each(newrow.keywords,function(k){%>
                                            <a href="<%=k.akey_link%>"><%=k.keyname%></a>
                                        <%})%> 
                                    <%}%>
                                    </div> 
                                <%}%> 
                                <%if(newrow.time){%>
                                    <span class="time"><%=formatTime(newrow.time)%></span>
                                <%}%> 
                            </div>
                            <div class="share-join clearfix">
                                <a class="post_recommend_tie right" href="<%=newrow.commenturl%>" >
                                    <div class="post_recommend_tie_wrap">
                                        <span class="post_recommend_tie_icon icons"><%=newrow.tienum%></span> 
                                        <span class="post_recommend_tie_text"><i>跟贴</i><%=newrow.tienum%></span>
                                    </div>
                                </a>
                                <div class="ne-shares-parent right">
                                    <span href="#share" title="分享" class="ne-shares-arr"></span>
                                    <div class="share-join-item" ne-module="/modules/shares/shares.js" ne-state="cls.hover:ne-shares-open;title:<%=newrow.title%>;url:<%=newrow.docurl%>;pic:<%=newrow.imgurl%>" >
<div class="ne-shares-pop6x1wrap" ne-role="share-wrap">
<ul class="ne-shares-pop6x1">
    <li>
        <a ne-click="share('yixin')" href="http://yixin.im/#f=www">
            <span class="inner">
                <i class="ep-share-icon ep-share-yixin"></i>
                <span class="ep-share-name">易信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-mouseover="initWeixin()" href="javascript:" target="_self" class="ne-shares-weixin">
            <span class="inner">
                <i class="ep-share-icon ep-share-weixin"></i>
                <span class="ep-share-name">微信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-click="share('sina')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-sina"></i>
                <span class="ep-share-name">微博</span>
            </span>
        </a>
    </li>
    <li class="last">
        <a ne-click="share('qzone')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-qzone"></i>
                <span class="ep-share-name">QQ空间</span>
            </span>
        </a>
    </li>
</ul>
</div>
<div class="ne-shares-qrwrap">
  <div class="ne-shares-qrarr"></div>
  <div ne-role="qrcode" class="ne-shares-qrcode"></div>
  <p>用微信扫码二维码</p><p>分享至好友和朋友圈</p>
</div>
</div>
                                </div>
                            </div>
                        </div>
                    </div>
                <%} else {%>
                    <div class="data_row news_article clearfix <%if(__i == 0){%>news_first<%}%>" i={{__i}}>
                        <div class="na_detail clearfix no_pic">
                            <div class="news_title">
                                <h3><a href="<%=newrow.docurl%>"><%=newrow.title%></a></h3>
                            </div>
                            <div class="news_tag">
                                <%if(newrow.channelname && newrow.channelname != "shehui" && newrow.channelname != "guonei" && newrow.channelname != "guoji" && newrow.channelname != "dada" && newrow.channelname != "war" && newrow.channelname != "hangkong"){%>
                                    <%if(newrow.tlastid != ""){%>
                                        <strong class="barlink"><%=newrow.tlastid%></strong>
                                    <%}else if(newrow.label != ""){%>
                                        <a href="<%=newrow.tlink%>" class="link link_more">
                                        <em><%=newrow.label%></em></a>
                                    <%}%> 
                                <%}%>
                                <%if(newrow.keywords && newrow.keywords.length > 0){%>
                                    <div class="keywords">
                                    <%bowlder.each(newrow.keywords,function(k){%>
                                        <a href="<%=k.akey_link%>"><%=k.keyname%></a>
                                    <%})%> 
                                    </div>
                                <%}%> 
                                <%if(newrow.time){%>
                                    <span class="time"><%=formatTime(newrow.time)%></span>
                                <%}%> 
                            </div>
                            <div class="share-join clearfix">
                                <a class="post_recommend_tie right" href="<%=newrow.commenturl%>" >
                                    <div class="post_recommend_tie_wrap">
                                        <span class="post_recommend_tie_icon icons"><%=newrow.tienum ? newrow.tienum : 0%></span> 
                                        <span class="post_recommend_tie_text"><i>跟贴</i><%=newrow.tienum%></span>
                                    </div>
                                </a>
                                <div class="ne-shares-parent right">
                                    <span href="#share" title="分享" class="ne-shares-arr"></span>
                                    <div class="share-join-item" ne-module="/modules/shares/shares.js" ne-state="cls.hover:ne-shares-open;title:<%=newrow.title%>;url:<%=newrow.docurl%>;pic:<%=newrow.imgurl%>" >
<div class="ne-shares-pop6x1wrap" ne-role="share-wrap">
<ul class="ne-shares-pop6x1">
    <li>
        <a ne-click="share('yixin')" href="http://yixin.im/#f=www">
            <span class="inner">
                <i class="ep-share-icon ep-share-yixin"></i>
                <span class="ep-share-name">易信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-mouseover="initWeixin()" href="javascript:" target="_self" class="ne-shares-weixin">
            <span class="inner">
                <i class="ep-share-icon ep-share-weixin"></i>
                <span class="ep-share-name">微信</span>
            </span>
        </a>
    </li>
    <li>
        <a ne-click="share('sina')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-sina"></i>
                <span class="ep-share-name">微博</span>
            </span>
        </a>
    </li>
    <li class="last">
        <a ne-click="share('qzone')" href="javascript:">
            <span class="inner">
                <i class="ep-share-icon ep-share-qzone"></i>
                <span class="ep-share-name">QQ空间</span>
            </span>
        </a>
    </li>
</ul>
</div>
<div class="ne-shares-qrwrap">
  <div class="ne-shares-qrarr"></div>
  <div ne-role="qrcode" class="ne-shares-qrcode"></div>
  <p>用微信扫码二维码</p><p>分享至好友和朋友圈</p>
</div>
</div>
                                </div>
                            </div>
                        </div>
                    </div>
                <%}%>
                </script>
            </div>
        </li>
    </ul>
    <div class="load_more_foot" id="load_more_foot"></div>
    <a class="load_more_btn" target="_self" ne-click="clickLoadMore();" ne-hide="{{myState.counter >= navList[myState.ndNavIndex].totalPage || myState.counter == 0}}">
       <div class="post_addmore" ne-visible="{{myState.counter < navList[myState.ndNavIndex].totalPage && !myState.loading}}">
           <i>+</i>
           <span>加载更多</span>
       </div>
       <div class="post_adding" ne-show="{{myState.loading}}">
           <i>+</i>
           <span>加载中...</span>
       </div>
    </a>
    <div class="load_more_tip" ne-show="{{myState.counter >= navList[myState.ndNavIndex].totalPage}}">:-)已经到最后啦~</div>
</div>
</div>
                        <!-- 信息流 结束 -->
                    </div>
                    <!-- 中间新闻 结束 -->
                    
                    <!-- 右侧栏目 开始 -->
                    <div class="main_right_channel">
                        <!-- 广告 -->
                        <!-- 300*30 -->
<!-- 新闻首页焦点图上方L特殊标识广告 开始-->
<!-- <div class="mod_newsr_ad1">
<a href="http://g.163.com/a?CID=45744&Values=2901173312&Redirect=http://clickc.admaster.com.cn/c/a73960,b1279435,c369,i0,m101,8a1,8b2,h"><img class="block mb10" width="300" height="30" src="http://img1.126.net/channel11/024018300301009.jpg" alt="广告"></a>
</div> -->
<!--新闻首页焦点图上方L特殊标识广告 结束-->
                        <!-- 焦点图 开始-->
                        <div class="mod_right_focus">
                            <div ne-module="">
<div class="mod_focus" ne-module="/modules/slide/slide.js" ne-state="slideMethod:left;events=mouseover;interval=4000;loop=true;">
    <div class="f_body" ne-role="slide-body">
        <!-- 新首右侧头图auditStart -->
        <ul class="f_main clearfix" ne-role="slide-scroll">
                                                                         <li ne-role="slide-page">
                <a href="http://news.163.com/photoview/00AP0001/2309372.html">
                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0718/90834355j00qdn71b000jc0008c00b4c.jpg?imageView&thumbnail=300y400" width="300" height="400">
                    <span class="bg"></span>
                    <h3>湖北恩施水位上涨 城区多处被淹</h3>
                </a>
            </li>
                                                             <li ne-role="slide-page">
                <a href="http://dy.163.com/article/FHQMIMTK0514R9P4.html">
                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0718/cca2a692j00qdng1l000oc0008c00b4c.jpg?imageView&thumbnail=300y400" width="300" height="400">
                    <span class="bg"></span>
                    <h3>武汉核酸检测医疗队启程支援新疆</h3>
                </a>
            </li>
                                                             <li ne-role="slide-page">
                <a href="https://news.163.com/20/0718/09/FHQDBRCT0001899O.html">
                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0718/44d3c506j00qdn6du005oc0008c00b4c.jpg?imageView&thumbnail=300y400" width="300" height="400">
                    <span class="bg"></span>
                    <h3>特朗普:不会发布全国性"口罩令"</h3>
                </a>
            </li>
                                                             <li ne-role="slide-page">
                <a href="http://news.163.com/photoview/00AP0001/2309364.html">
                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/5682e1c6j00qdm8k4000yc0008c00b4c.jpg?imageView&thumbnail=300y400" width="300" height="400">
                    <span class="bg"></span>
                    <h3>长江重庆段水位上涨临江商铺转移</h3>
                </a>
            </li>
                    </ul>
        <!-- 新首右侧头图auditEnd -->
    </div>
    <div class="f_title">
                        <span ne-role="slide-nav" class="current  ">1</span>
                <span ne-role="slide-nav" class=" ">2</span>
                <span ne-role="slide-nav" class=" ">3</span>
                <span ne-role="slide-nav" class=" ">4</span>
            </div>
    <a ne-role="slide-prev" class="f_prev">&lt;</a>
    <a ne-role="slide-next" class="f_next">&gt;</a>
</div>
</div>
                        </div>
                        <!-- 焦点图 结束-->
                        <!-- 广告 开始-->
                        <div class="mod_ad_toutu channel_relative_2016">
                            <ul class="clearfix">
                                <li><a href="https://hongcai.163.com/?from=pcsy-button">专业竞彩一触即发</a></li>
<li><a href="https://open.163.com/">让分享知识成为习惯</a></li>
<li><a href="https://vip.open.163.com/courses/2243?p=home_discount_order_pc">会说话的人生能开挂</a></li>
<li><a href="http://renjian.163.com/special/renjian_kanke/">不止是看客</a></li>
                            </ul>
                            <span class="channel_ad_text_2016">广告</span>
                        </div>
                        <!-- 广告 结束-->
                        <!-- 右侧960原创栏目 开始 -->
                        <div class="origina_column_960" id="js_origina_column_960">
                            <div ne-module="/news/index2016_rmd/modules/originacolumn/originacolumn.js">
<div class="origina_column_warp">
	<h2>
		<span>新闻各有态度</span>
	</h2>
    <div class="scroll_bd" ne-role="scroll_bd">
        <div class="scroll_column_bd">
            <ul class="scroll_ul">
                <!-- 回声 开始 -->
            
                <!-- 回声 结束 -->
                <!-- 数读 开始 -->
                <li class="cell cell_sd cell_hover">
                    <p class="tag_line">
                        <a href="http://data.163.com/special/datablog/" class="tags tag_sd">数读</a>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://data.163.com/20/0717/20/FHP08AB1000181IU.html" class="detail" ne-role="detail">
                            <h3>
                                从虎扑女神大赛看，直男审美如何
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/3f17be23j00qdm5gk00atc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="从虎扑女神大赛看，直男审美如何">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://data.163.com/20/0713/14/FHE3R5UN00019GOE.html">山西女孩可爱第一名，吃醋第二名</a></li>
                                                        <li class="twoli "><a href="http://data.163.com/20/0712/22/FHC9QSVC000181IU.html">中国最爱下雨的地方是哪里</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 数读 结束 -->
                <!-- 人间 开始 -->
                <li class="cell cell_rj">
                    <p class="tag_line">
                        <a href="http://renjian.163.com/" class="tags tag_rj">人间</a>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://renjian.163.com/20/0717/10/FHNT47LF000181RV.html" class="detail" ne-role="detail">
                            <h3>
                                一进看守所，他就“精神病”了
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/845e9b12j00qdle0k001cc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="一进看守所，他就“精神病”了">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://renjian.163.com/20/0714/11/FHG9I2FT000181RV.html">被人言说散的换肾夫妻</a></li>
                                                        <li class="twoli "><a href="http://renjian.163.com/20/0709/16/FH40K5UP000181RV.html">人间这场局，谁能置身事外</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 人间 结束 -->
                <!-- 大国小民 开始 -->
                <li class="cell cell_dgxm">
                    <p class="tag_line">
                        <span class="tags tag_dgxm">大国小民</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://renjian.163.com/20/0715/10/FHIOM7VT000181RK.html" class="detail" ne-role="detail">
                            <h3>
                                为女相亲，小夏的人民公园历险记
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/fc1f0ea6j00qdhp25001oc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="为女相亲，小夏的人民公园历险记">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://renjian.163.com/20/0714/17/FHGTCP1P000181RK.html">在温哥华倒腾房子，我越买越穷</a></li>
                                                        <li class="twoli "><a href="http://renjian.163.com/20/0713/10/FHDKK2C0000181RK.html">工地上，那个被歧视的新手白领</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 大国小民 结束 -->
                <!-- 三三有梗 开始 -->
                <!-- 三三有梗 结束 -->
                <!-- 三三映画 开始 -->
                <!-- 三三映画 结束 -->
                <!-- 我去1990 开始 -->
                <!-- 我去1990 结束 -->
                <!-- 轻松一刻 开始 -->
                <li class="cell cell_qsyk">
                    <p class="tag_line">
                        <span class="tags tag_qsyk">轻松一刻</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="https://news.163.com/20/0717/18/FHONVAP7000181BR.html" class="detail" ne-role="detail">
                            <h3>
                                小心！你的手机里可能有个“窃贼”
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/1d17eb76j00qdlzxa000pc0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="小心！你的手机里可能有个“窃贼”">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="https://news.163.com/20/0716/19/FHMAKRIT000181BR.html">"童养媳"都知道,"童养夫"还是头次听说</a></li>
                                                        <li class="twoli "><a href="https://news.163.com/20/0714/19/FHH63Q22000181BR.html">迷惑!SPA店诱惑顾客充值,却提供正规服务</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 轻松一刻 结束 -->
                <!-- 槽值 开始 -->
                <li class="cell cell_caozhi">
                    <p class="tag_line">
                        <span class="tags tag_caozhi">槽值</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="http://caozhi.news.163.com/20/0715/18/FHJJDKJB000181TI.html" class="detail" ne-role="detail">
                            <h3>
                                韩寒怎么就走到了这一步
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/6b6360dcj00qdi9tx003tc000go005kc.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="韩寒怎么就走到了这一步">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://caozhi.news.163.com/20/0714/18/FHH120V1000181TI.html">那些藏起胸部的中国女孩</a></li>
                                                        <li class="twoli "><a href="http://caozhi.news.163.com/20/0713/15/FHE4FOBC000181TI.html">500块一瓶的眼霜，没有平价替代</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 槽值 结束 -->
                <!-- 谈心社 开始 -->
                <li class="cell cell_tanxinshe">
                    <p class="tag_line">
                        <span class="tags tag_tanxinshe">谈心社</span>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="https://news.163.com/20/0716/13/FHLM15JA0001982T.html" class="detail" ne-role="detail">
                            <h3>
                                德云社的“门面担当”，凭什么是他？
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0716/26614933j00qdjrkd002jc000go005kc.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="德云社的“门面担当”，凭什么是他？">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="https://news.163.com/20/0716/15/FHLSK89L0001982T.html">16岁天才少女爆红，谁在制造神童</a></li>
                                                        <li class="twoli "><a href="https://news.163.com/20/0715/15/FHJB0TGM0001982T.html">40岁的陈冠希，你怎么老成这样了？</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 谈心社 结束 -->
                <!-- 看客 开始 -->
                <li class="cell cell_kanke">
                    <p class="tag_line">
                        <a href="http://renjian.163.com/special/renjian_kanke/" class="tags tag_kanke">看客</a>
                    </p>
                    <div class="column_main">
                                                                                                                                                                                         <a href="http://renjian.163.com/20/0716/09/FHL99JGS000199ET.html" class="detail" ne-role="detail">
                            <h3>
                                毕业后，我在新媒体公司卖性药
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0716/920ffc37p00qdjm01002qc0009c005uc.png?imageView&thumbnail=200y90" width="200" height="90" alt="毕业后，我在新媒体公司卖性药">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="http://renjian.163.com/20/0714/10/FHG6B13P000199ET.html">麻风病人被隔离的半个世纪</a></li>
                                                        <li class="twoli "><a href="http://renjian.163.com/20/0713/10/FHDKBVHA000199ET.html">暴富梦碎后，他们原地卖起了房</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 看客 结束 -->
                <!-- 身体密码 开始 -->
                <li class="cell cell_stpwd">
                    <p class="tag_line">
                        <a href="http://jiankang.163.com/special/zhutierji/?type=3" class="tags tag_stpwd">身体密码</a>
                    </p>
                    <div class="column_main">
                                                                                                                         <a href="https://jiankang.163.com/20/0706/17/FGSD8J9A00388AD5.html" class="detail" ne-role="detail">
                            <h3>
                                每年疼哭300万人的病 终于有疫苗了！
                            </h3>
                            <div class="photo">
                                <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0707/abc0f48bj00qd2wmt0008c0005k002ic.jpg?imageView&thumbnail=200y90" width="200" height="90" alt="每年疼哭300万人的病 终于有疫苗了！">
                            </div>
                        </a>
                                                <ul>
                                                                                    <li class=""><a href="https://jiankang.163.com/20/0623/18/FFR0JAOA00388AD5.html">男生玩阿鲁巴是一种怎样的体验</a></li>
                                                        <li class="twoli "><a href="https://jiankang.163.com/20/0604/09/FE94EET40038804G.html">科学化解"人生之气"带来的尴尬</a></li>
                                                    </ul>
                    </div>
                </li>
                <!-- 身体密码 结束 -->
                <!-- 哒哒 开始 -->
            
                <!-- 哒哒 结束 -->
            </ul>
        </div>
        <div id="js_baseline"></div>
        <span class="white_bg" id="js_white_bg"></span>
    </div>
</div>
</div>
                        </div>
                        <!-- 右侧960原创栏目 结束 -->
                        <div class="mt12 mod_ad_1 mod_ad_r">
                            <!-- 300*250 -->
<div class="at_item right_ad_item" adType="rightAd" requestUrl="https://nex.163.com/q?app=7BE0FC82&c=news&l=31&site=netease&affiliate=news&cat=homepage&type=logo300x250&location=1"></div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                        <!-- 新闻策划 开始 -->
                        <div class="mt35 mod_pageh5" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div ne-module="/news/index2016_rmd/modules/modh5/modh5.js">
<div class="idx_cm_title">
	<a href="https://open.163.com/" class="title">网易公开课</a>
</div>
<div class="wrap" ne-module="/modules/slide/slide.js" ne-state="slideMethod:left;events=mouseover;interval=4000;loop=true;">
	<div class="h5_bg h5_border">
		<div class="h5_body" ne-role="slide-body">
			<div class="h5_main clearfix" ne-role="slide-scroll">
				                                                         				<div ne-role="slide-page" class="h5_item">
					<div class="h5_item_poster">
						<a href="http://open.163.com/newview/movie/courseintro?newurl=SE9RR3BEI#share-mob">
							<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/54c09bc2j00qdhr8n000rc0007s00c4c.jpg?imageView&thumbnail=280y436" width="280" height="436">
							<span class="bg"></span>
							<h3>为何有人总是很年轻？</h3>
						</a>
					</div>
				</div>
				                                         				<div ne-role="slide-page" class="h5_item">
					<div class="h5_item_poster">
						<a href="http://open.163.com/newview/movie/courseintro?newurl=VDJTIESIL#share-mob">
							<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/fdbcb4c0j00qdhp330014c0007s00c4c.jpg?imageView&thumbnail=280y436" width="280" height="436">
							<span class="bg"></span>
							<h3>网红经济的背后，有我这样的经纪人</h3>
						</a>
					</div>
				</div>
				                                         				<div ne-role="slide-page" class="h5_item">
					<div class="h5_item_poster">
						<a href="http://open.163.com/newview/movie/courseintro?newurl=VEAO8D867#share-mob">
							<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0713/c017ebcbj00qdek960012c0007s00c4c.jpg?imageView&thumbnail=280y436" width="280" height="436">
							<span class="bg"></span>
							<h3>有哪些意想不到的赚钱行业？</h3>
						</a>
					</div>
				</div>
				                                         				<div ne-role="slide-page" class="h5_item">
					<div class="h5_item_poster">
						<a href="http://open.163.com/newview/movie/courseintro?newurl=TEIUTNPMD#share-mob">
							<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0713/789744eaj00qdek7y000gc0007s00c4c.jpg?imageView&thumbnail=280y436" width="280" height="436">
							<span class="bg"></span>
							<h3>一周不吃糖，身体会怎样？</h3>
						</a>
					</div>
				</div>
							</div>
			<span class="ad_hover_pic">广告</span>
		</div>
		<!-- <div class="scrollbtn scrollbtl" ne-role="scrollbtn"><a ne-role="slide-prev" class="f_prev">&lt;</a></div>
		<div class="scrollbtn scrollbtnr" ne-role="scrollbtn"><a ne-role="slide-next" class="f_next">&gt;</a></div> -->
		<div class="nav clearfix">
			<span ne-role="slide-nav" ne-repeat="1..state.total"></span>
		</div>
	</div>
	<!-- <div class="nav clearfix">
		<span ne-role="slide-nav" ne-repeat="1..state.total"></span>
	</div> -->
</div></div>
                        </div> 
                        <!-- 新闻策划 结束 -->
                        <!-- 新闻专题 开始 -->
                        <div class="mt30 mod_news_special" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title"><a href="http://news.163.com/special/">新闻专题</a></h2>
                            </div>
                            <div class="bd">
                                                                                                                                                         <div class="photo">
                                    <a href="https://news.163.com/special/2020qglh/">
                                        <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0604/7ef9d4f0j00qbe9w1006sc0008c002ic.jpg?imageView&thumbnail=300y90" width="300" height="90" alt="2020年全国两会">
                                    </a>
                                </div>
                                <h3>    
                                    <span>HOT</span>
                                    <strong><a href="https://news.163.com/special/2020qglh/">2020年全国两会</a></strong>
                                </h3>
                                                                <ul class="idx_cm_list">
                                                                                                            <li>
                                        <a href="http://news.163.com/special/2020chunyun/#photo">2020年春运春节</a>
                                    </li>
                                                                        <li>
                                        <a href="http://news.163.com/special/zgdj_70/">中国答卷-新中国成立70周年</a>
                                    </li>
                                                                        <li>
                                        <a href="http://news.163.com/special/zghj70/">海军成立70周年</a>
                                    </li>
                                                                        <li>
                                        <a href="http://news.163.com/special/2019qglh/">2019年全国两会</a>
                                    </li>
                                                                    </ul>
                            </div>
                        </div>
                        <!-- 新闻专题 结束 -->
                        <!-- 高层动态 开始-->
                        <!-- 高层动态 结束-->
                        
                        <div class="mt25 mod_ad_2 mod_ad_r">
                            <!-- 300*250 -->
<div class="at_item right_ad_item" adType="rightAd" requestUrl="https://nex.163.com/q?app=7BE0FC82&c=news&l=32&site=netease&affiliate=news&cat=homepage&type=logo300x250&location=2"></div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                        <!-- 军事 航空  开始 -->
                        <div class="mt35 mod_war" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title">
                                    <a href="http://war.163.com/">军事</a>
                                    <i>·</i>
                                    <a href="http://news.163.com/air/">航空</a>
                                </h2>
                            </div>
                                                                                                                                                                         <div class="idx_cm_img">
                                <a href="http://war.163.com/photoview/4T8E0001/2309366.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0718/fdea5999j00qdn1ns0031c000s600e3c.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="两栖攻击舰的黎波里号入役">
                                    <div class="bg">
                                        <h3>两栖攻击舰的黎波里号入役</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="http://war.163.com/photoview/4T8E0001/2309369.html">双航母战斗群再闯南海</a>
                                </li>
                                                                <li>
                                    <a href="http://war.163.com/photoview/4T8E0001/2309365.html">实弹射击，火力全开</a>
                                </li>
                                                                                                <li>
                                    <a href="http://news.163.com/air/photoview/56NT0001/2309371.html">停在西班牙飞机墓地里的民航客机</a>
                                </li>
                                                                <li>
                                    <a href="http://news.163.com/air/photoview/56NT0001/2309370.html">澳航对波音747的最后告别</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 军事 航空  结束 -->
                        <div class="mt27 mod_ad_3 mod_ad_r">
                            <!-- 300*250 -->
<div class="at_item" >
<!-- 广告位：网易-新闻频道-首页-M3 -->
<div id="ssp_6905141"></div>
<script>
(function() {
    (window.slotbydup=window.slotbydup || []).push({
        id: '6905141',
        container: 'ssp_6905141',
        size: '300,250',
        display: 'inlay-fix',
        async: true
    });
})();
</script>
</div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                        <!-- 热点排行 开始 -->
                        <div class="mt35 mod_hot_rank clearfix" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <a href="http://news.163.com/rank/" class="title">热点排行</a>
                            </div>
                            <ul>
                                                                                                <li class="top ">
                                    <em>1</em>
                                    <a href="https://news.163.com/20/0717/16/FHOIKBS70001899O.html">浙江男子持刀在教室杀死女儿9岁同学 被执行死刑</a>
                                    <span>189355</span>
                                </li>
                                                                <li class=" top ">
                                    <em>2</em>
                                    <a href="https://news.163.com/20/0717/21/FHP293RK0001899O.html">母女被困电梯4天互喝尿液求生:住4层别墅 没带手机 </a>
                                    <span>90544</span>
                                </li>
                                                                <li class=" top ">
                                    <em>3</em>
                                    <a href="https://news.163.com/20/0717/16/FHOHHAMF0001899O.html">男子将30万现金放电梯里喊家人来拿 门开了钱没了</a>
                                    <span>46833</span>
                                </li>
                                                                <li class="">
                                    <em>4</em>
                                    <a href="https://news.163.com/20/0717/19/FHOT9KU00001899O.html">乌鲁木齐居民:收到物业"小区人员不允许进出"信息 </a>
                                    <span>44160</span>
                                </li>
                                                                <li class="">
                                    <em>5</em>
                                    <a href="https://news.163.com/20/0718/11/FHQJHHHM0001899O.html">乌鲁木齐全市正做核酸检测 12日半夜就有人被隔离</a>
                                    <span>33192</span>
                                </li>
                                                                <li class="">
                                    <em>6</em>
                                    <a href="https://news.163.com/20/0717/22/FHP7502T0001899O.html">乌鲁木齐市内社区进行封闭管理 有居民开始居家办公</a>
                                    <span>28087</span>
                                </li>
                                                                <li class="">
                                    <em>7</em>
                                    <a href="https://news.163.com/20/0718/09/FHQDUPCI0001899O.html">13岁女孩遭8旬老人性侵怀孕 一家四口均有精神障碍</a>
                                    <span>22150</span>
                                </li>
                                                                <li class="">
                                    <em>8</em>
                                    <a href="https://news.163.com/20/0717/14/FHOBI6680001899O.html">新疆新增新冠肺炎确诊病例5例 无症状感染者8例</a>
                                    <span>17309</span>
                                </li>
                                                                <li class="">
                                    <em>9</em>
                                    <a href="https://news.163.com/20/0718/02/FHPKC49H0001899O.html">莫斯科市市长：60%的莫斯科市民已获得群体免疫</a>
                                    <span>11372</span>
                                </li>
                                                                <li class="">
                                    <em>10</em>
                                    <a href="http://v.163.com/paike/VF504532M/VZGQSQ9QK.html">1998年到现在，20年过去了，中国的抗洪能力变强了吗？</a>
                                    <span>8486</span>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 热点排行 结束 -->
                        <div class="mt25 mod_ad_4 mod_ad_r">
                            <!-- 300*250 -->
<div class="at_item" >
<!-- 广告位：网易-新闻频道-首页-M4 -->
<div id="ssp_6905142"></div>
<script>
(function() {
    (window.slotbydup=window.slotbydup || []).push({
        id: '6905142',
        container: 'ssp_6905142',
        size: '300,250',
        display: 'inlay-fix',
        async: true
    });
})();
</script>
</div>
                        </div>
                        <!-- 财经 开始 -->
                        <div class="mt35 mod_money" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title"><a href="http://money.163.com/">财经</a></h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="https://money.163.com/20/0717/07/FHNKMH4K00259DLP.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/91664630p00qdl6pk003tc0008d0046c.png?imageView&thumbnail=300y150" width="300" height="150" alt="猛降400万!深圳房市降价潮来了?">
                                    <div class="bg">
                                        <h3>猛降400万!深圳房市降价潮来了?</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="https://money.163.com/20/0717/07/FHNKF3GS00259DLP.html">蚂蚁财富数据出错？基民昨日损失惨重</a>
                                </li>
                                                                <li>
                                    <a href="https://money.163.com/20/0717/07/FHNK865900258152.html">“嘀哩嘀哩”创始人被批捕</a>
                                </li>
                                                                <li>
                                    <a href="https://money.163.com/20/0717/07/FHNK1ENB00258152.html">格力实施史上首次回购 董明珠嗅到了什么?</a>
                                </li>
                                                                <li>
                                    <a href="https://money.163.com/20/0717/06/FHNG6P4F002580S6.html">美股下挫 被315点名趣头条重挫23.0%</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 财经 结束 -->
                        <!-- 体育 开始 -->
                        <div class="mt27 mod_sports" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title"><a href="http://sports.163.com/">体育</a></h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="http://sports.163.com/photoview/3SLH0005/167826.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/656c3e8ej00qdllnz000fc0008c005kc.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="傅园慧现身长沙机场 背皮卡丘颈枕">
                                    <div class="bg">
                                        <h3>傅园慧现身长沙机场 背皮卡丘颈枕</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="http://sports.163.com/nba/">乔治:我爱LA 喜欢和LBJ一起打球</a>
                                </li>
                                                                <li>
                                    <a href="http://sports.163.com/18/0613/03/DK5AC8750005877U.html">格林:3年前降薪就在等KD</a> <a target="_blank" href="http://sports.163.com/18/0613/06/DK5L3C180005877U.html">特制T恤嘲讽LBJ</a>
                                </li>
                                                                <li>
                                    <a href="http://sports.163.com/18/0613/11/DK679LN20005877U.html">塔克4000双鞋让保罗羡慕嫉妒 乔丹被震惊</a>
                                </li>
                                                                <li>
                                    <a href="http://sports.163.com/cba/">CBA下季新赛制:常规赛4组循环 增至46轮</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 体育 结束 -->
                        <div class="mt27 mod_ad_5 mod_ad_r" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <!-- 300*250 -->
<div class="at_item" >
<!-- 广告位：网易-新闻频道-首页-M5 -->
<div id="ssp_6905143"></div>
<script>
(function() {
    (window.slotbydup=window.slotbydup || []).push({
        id: '6905143',
        container: 'ssp_6905143',
        size: '300,250',
        display: 'inlay-fix',
        async: true
    });
})();
</script>
</div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                        
                        <!-- 娱乐 开始 -->
                        <div class="mt35 mod_ent" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title"><a href="http://ent.163.com/">娱乐</a></h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="http://ent.163.com/photoview/00AJ0003/676502.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0718/1123529dp00qdn57a002rc0008c0046c.png?imageView&thumbnail=300y150" width="300" height="150" alt="王鸥穿抹胸裙秀身材">
                                    <div class="bg">
                                        <h3>王鸥穿抹胸裙秀身材</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="https://ent.163.com/20/0718/08/FHQB716D00038FO9.html">罗志祥近况曝光：健身保持身材 进军餐饮业</a>
                                </li>
                                                                <li>
                                    <a href="https://ent.163.com/20/0718/08/FHQ8KCCA00038FO9.html">江疏影20岁军训旧照曝光 身形瘦削皮肤白皙</a>
                                </li>
                                                                <li>
                                    <a href="https://ent.163.com/20/0718/07/FHQ5VMG500038FO9.html">被猜测离婚 李玟再度发文：练习去乐观  </a>
                                </li>
                                                                <li>
                                    <a href="https://ent.163.com/20/0718/08/FHQANUD700038FO9.html">蔡徐坤手拉张大大跑步 画风搞笑成偶像剧</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 娱乐 结束 -->
                        
                        <!-- 汽车精选 开始 -->
                        <div class="mt25 mod_auto" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title"><a href="http://auto.163.com/">汽车精选</a></h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="https://auto.163.com/20/0717/10/FHNTC1M80008856R.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0718/ae7117fbj00qdn8x90007c0008c0050c.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="丰田新凯美瑞前脸采用了新的设计">
                                    <div class="bg">
                                        <h3>丰田新凯美瑞前脸采用了新的设计</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="https://auto.163.com/20/0718/09/FHQE0I4T0008856R.html">更大内饰显豪华 全新哈弗H6将于24日首发 </a>
                                </li>
                                                                <li>
                                    <a href="https://auto.163.com/20/0717/10/FHNTD4I70008856R.html">2.7秒破百 保时捷新911 Turbo官图发布</a>
                                </li>
                                                                <li>
                                    <a href="https://auto.163.com/20/0718/09/FHQE28G00008856R.html">野性十足的SUV 2020款北京BJ80预售35万</a>
                                </li>
                                                                <li>
                                    <a href="https://auto.163.com/20/0717/20/FHP0C1UU0008856R.html">东风高端电动品牌定名"岚图" 明年推新车</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 购车指南 结束 -->
                        <div class="mt25 mod_ad_6 mod_ad_r">
                            <!-- 300*250 -->
<div class="at_item" >
<!-- 广告位：网易-新闻频道-首页-M6 -->
<div id="ssp_6905144"></div>
<script>
(function() {
    (window.slotbydup=window.slotbydup || []).push({
        id: '6905144',
        container: 'ssp_6905144',
        size: '300,250',
        display: 'inlay-fix',
        async: true
    });
})();
</script>
</div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                        <!-- 房产 开始 -->
                        <div class="mt35 mod_house" ne-module="/news/index2016_rmd/modules/house/house.js" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}"><script type="text/template" ne-repeat="vhouse in rhouselist">    
<div class="idx_cm_title">
    <h2 class="title">
        <a href="<%=vhouse.houselink%>">房产</a>
        <i>·</i>
        <a href="http://home.163.com/">家居</a>
    </h2>
    <%if(vhouse.moresecondary){%>
    <a class="more" href="<%=vhouse.moresecondary%>">二手房</a>
    <%}%>
    <a class="more" href="<%=vhouse.moreloupan%>">楼盘大全</a>
</div>
<div class="idx_cm_img">
    <a href="<%=vhouse.imgdocurl%>">
        <img src="<%=vhouse.imgs%>?imageView&thumbnail=300y150&quality=85" width="300" height="150" alt="<%=vhouse.imgstitle%>">
        <div class="bg">
            <h3><%=vhouse.imgstitle%></h3>
        </div>
    </a>
</div>
<ul class="mt12 idx_cm_list idx_cm_list_h">
    <%if(vhouse.news){%>
    <%for(var i=0;i<vhouse.news.length;i++){%>
        <li><a href="<%=vhouse.news[i].link%>"><%=vhouse.news[i].title%></a></li>
    <%}%><%}%>
</ul>
</script>
<ul class="idx_cm_list idx_cm_list_h">
                 <li><a href="https://home.163.com/20/0718/08/FHQB0T4800108GL2.html">阿联酋总统身家1654亿 光在伦敦就有140套豪宅</a></li>
             <li><a href="https://home.163.com/20/0718/08/FHQ9DHN300108GL2.html">美女参观尼泊尔土豪别墅 造价2800万全屋木雕花</a></li>
    </ul>
</div>
                        <!-- 房产 结束 -->
                        <div class="mt27 mod_ad_7 mod_ad_r">
                            <!-- 300*250 -->
<div style="position:relative;height:250px;">
  <a href="http://gb.corp.163.com/gb/legal.html" class="ad_hover_href"></a>
<!-- 广告位：网易-新闻频道--频道首页--矩形M7-M大画面广告 -->
<div id="ssp_6374355"></div>
<script>
  (function() {
      (window.slotbydup=window.slotbydup || []).push({
          id: '6374355',
          container: 'ssp_6374355',
          size: '300,250',
          display: 'inlay-fix',
          async:true
      });
  })();
  </script>
  <script async _src="//dup.baidustatic.com/js/os.js" id="baiduad"></script>
</div>
                        </div>
                        <!-- 精彩视频 开始-->
                        <div class="mt35 mod_wonderful_video" ne-module="/news/index2016_rmd/modules/live/live.js" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}"><div class="idx_cm_title">
    <a href="http://v.163.com/" class="title">精彩直播</a>
</div>
<script type="text/template" ne-repeat="livetop in topLive">
<a href="http://live.163.com/room/<%=livetop.roomId%>.html" class="big_video" title="<%=livetop.roomName%>">
    <img src="<%=livetop.pcImage%>?imageView&thumbnail=350y190" alt="<%=livetop.roomName%>" title="<%=livetop.roomName%>" width="350" height="190"> 
    <span class="bg"></span>
    <em></em>
    <span class="title"><%=livetop.roomName%></span>
</a>
</script>
<div class="clearfix small_video">
<script type="text/template" ne-repeat="live in liveList">
    <a href="http://live.163.com/room/<%=live.roomId%>.html" class="item" title="<%=live.roomName%>">
        <img src="<%=live.pcImage%>?imageView&thumbnail=190y88&quality=85" alt="<%=live.roomName%>" title="<%=live.roomName%>" width="190" height="88">
        <h3 class="item_text"><%=live.roomName%><i class="icon_video"></i></h3>
        
    </a>
</script>
</div>  </div>
                        <!-- 精彩视频 结束-->
                        <!-- 科技 开始 -->
                        <div class="mt35 mod_tech" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title"><a href="http://tech.163.com/">科技</a></h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="https://tech.163.com/20/0715/07/FHIEVV7K00097U7S.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0715/8ae39dcbj00qdhjyg001lc000mc00ckc.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="美国再打击华为，英政府决定是雪上加霜">
                                    <div class="bg">
                                        <h3>美国再打击华为，英政府决定是雪上加霜</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                 <li>
                                    <a href="https://tech.163.com/special/S1594897622471/">趣头条宣布整改：广告运营负责人停职</a>
                                </li>
                                                                <li>
                                    <a href="https://tech.163.com/20/0717/07/FHNKP10400097U7R.html">当当法务部：李国庆只是小股东</a>
                                </li>
                                                                <li>
                                    <a href="https://tech.163.com/20/0717/07/FHNKIVD100097U7R.html">有内鬼？！推特号被盗 CEO称将透明调查</a>
                                </li>
                                                                <li>
                                    <a href="https://tech.163.com/20/0717/08/FHNLRMN400097U80.html">欧盟拟对Alexa等语音助手做反垄断调查</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 科技 结束 -->
                        <!-- 手机 数码  开始 -->
                        <div class="mt27 mod_digi" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title">
                                    <a href="http://mobile.163.com/">手机</a>
                                    <i>·</i>
                                    <a href="http://digi.163.com/">数码</a>
                                </h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="https://mobile.163.com/20/0717/03/FHN5S7S900119821.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/24bc8fc7j00qdlg2w0023c000go00b4c.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="iPhone 12会将成本控制到极致">
                                    <div class="bg">
                                        <h3>iPhone 12会将成本控制到极致</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="https://mobile.163.com/20/0717/03/FHN5MG8000119821.html">苹果扩大iPhone等产品服务</a>
                                </li>
                                                                <li>
                                    <a href="https://mobile.163.com/20/0717/02/FHN2H5DQ00119821.html">苹果A14性能更加无敌</a>
                                </li>
                                                                                                <li>
                                    <a href="https://digi.163.com/20/0718/09/FHQEJGH7001697V8.html">macOS换ARM来势汹汹 Win10 ARM失败在哪里</a>
                                </li>
                                                                <li>
                                    <a href="https://digi.163.com/20/0718/10/FHQET9IO001697V8.html">支持5G的iPad Pro明年年初发布：使用mini-LED背光</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 手机 数码  结束 -->
                        <div class="mt27 mod_ad_8 mod_ad_r">
                            <!-- 300*250 -->
<div style="position:relative;height:250px;">
  <a href="http://gb.corp.163.com/gb/legal.html" class="ad_hover_href"></a>
<iframe class="fl cmIframe_js_ad"  _src="https://g.163.com/r?site=netease&affiliate=news&cat=homepage&type=logo300x250&location=8" width="300" height="250" frameborder="no" border="0" marginwidth="0" marginheight="0" scrolling="no"></iframe>
</div>
                        </div>
                        <!-- 女人时尚 开始 -->
                        <div class="mt35 mod_lady" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title">
                                    <a href="http://lady.163.com/">女人</a>
                                    <i>·</i>
                                    <a href="http://fashion.163.com/">时尚</a>
                                </h2>
                            </div>
                                                                                                                                                                         <div class="idx_cm_img">
                                <a href="https://lady.163.com/20/0717/21/FHP3185000267VQQ.html">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0717/850b785ep00qdlz3n00r6c000s600e3c.png?imageView&thumbnail=300y150" width="300" height="150" alt="看完51岁珍妮弗·洛佩兹这身材和状态我酸了！">
                                    <div class="bg">
                                        <h3>看完51岁珍妮弗·洛佩兹这身材和状态我酸了！</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="http://lady.163.com/photoview/00A70026/117454.html#p=FHQARNB100A70026NOS">短发阚清子换上双马尾造型录节目 甜度爆表</a>
                                </li>
                                                                <li>
                                    <a href="http://dy.163.com/article/FHLLNHN00518D9C7.html">Jennie碧梨的双色挑染发型你敢尝试么？</a>
                                </li>
                                                                <li>
                                    <a href="http://dy.163.com/article/FHQ8UG2L0538A2ZJ.html">方领连衣裙这样搭配 简约大方显气质</a>
                                </li>
                                                                <li>
                                    <a href="http://dy.163.com/article/FHPLTOVF051885FE.html">虽然是精神病但是长得美就没关系？</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 女人时尚 结束 -->
                        <!-- 教育 旅游  开始 -->
                        <div class="mt27 mod_edu" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title">
                                    <a href="http://edu.163.com/">教育</a>
                                    <i>·</i>
                                    <a href="http://travel.163.com/">旅游</a>
                                </h2>
                            </div>
                                                                                                                                                                         <div class="idx_cm_img">
                                <a href="https://edu.163.com/special/2020gaokaoreport/">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0627/be48939bj00qckuhc00ayc000s600e3c.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="2020年网易教育高考报道">
                                    <div class="bg">
                                        <h3>2020年网易教育高考报道</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="https://edu.163.com/20/0718/08/FHQ8LRN100297VGM.html">陈同学父亲致歉，他的"过度参与"涉嫌犯罪吗？</a>
                                </li>
                                                                <li>
                                    <a href="https://edu.163.com/20/0718/07/FHQ4K1V500297VGM.html">严查作弊 浙江12名考生高考成绩无效</a>
                                </li>
                                                                                                <li>
                                    <a href="https://travel.163.com/20/0718/00/FHPCIVJK00068AIR.html">日本将启动旅游支援项目 东京疫情反弹</a>
                                </li>
                                                                <li>
                                    <a href="https://travel.163.com/20/0718/00/FHPCIV5200068AIR.html">秦淮河畔南京城 </a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 教育 移民  结束 -->
                        <!-- 健康 读书 开始 -->
                        <div class="mt27 mod_jiankang" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                            <div class="idx_cm_title">
                                <h2 class="title">
                                    <a href="http://jiankang.163.com/">健康</a>
                                    <i>·</i>
                                    <a href="http://yuedu.163.com/">读书</a>
                                </h2>
                            </div>
                                                                                                                                         <div class="idx_cm_img">
                                <a href="http://jiankang.163.com">
                                    <img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="https://cms-bucket.ws.126.net/2020/0716/8f5ebcfbj00qdjxtn00d2c0008c0046c.jpg?imageView&thumbnail=300y150" width="300" height="150" alt="围观疫情之下的解暑“新招数”">
                                    <div class="bg">
                                        <h3>围观疫情之下的解暑“新招数”</h3>
                                    </div>
                                </a>
                            </div>
                                                        <ul class="mt12 idx_cm_list idx_cm_list_h">
                                                                                                <li>
                                    <a href="http://caiwei.yuedu.163.com/">为孩子辞职在家 丈夫却另结新欢</a>
                                </li>
                                                                <li>
                                    <a href="http://guofeng.yuedu.163.com/">拒绝购买iPhoneX 女友提出分手</a>
                                </li>
                                                                                                <li>
                                    <a href="https://jiankang.163.com/20/0716/17/FHM4VUN200388045.html">北京新发地疫情及关联传播已基本终止</a>
                                </li>
                                                                <li>
                                    <a href="https://jiankang.163.com/20/0716/15/FHLT3LL000388051.html">减肥贴、暖宫贴……这些贴大多是忽悠</a>
                                </li>
                                                            </ul>
                        </div>
                        <!-- 健康 读书 结束 -->
                        <div class="mt27 mod_ad_9 mod_ad_r">
                            <!-- 300*250 -->
<div class="at_item" >
  <!-- 广告位：网易-新闻频道-首页-M9 -->
<div id="ssp_6905146"></div>
<script>
(function() {
    (window.slotbydup=window.slotbydup || []).push({
        id: '6905146',
        container: 'ssp_6905146',
        size: '300,250',
        display: 'inlay-fix',
        async: true
    });
})();
</script>
</div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                        <span id="js_rfix_baseline"></span>
                        <div class="mt30 mod_ad_10 mod_ad_r" id="js_right_last">
                            <!-- 300*250 -->
<div class="at_item right_ad_item" adType="rightAd" requestUrl="https://nex.163.com/q?app=7BE0FC82&c=news&l=40&site=netease&affiliate=news&cat=homepage&type=logo300x250&location=10"></div>
<a href="javascript:;" target="_self" class="ad_hover_href"></a>
                        </div>
                    </div>
                    <!-- 右侧栏目 结束 -->
                </div>
                <!-- 内容区域 结束 -->
                <!--!include collector="first"-->
                <!-- 博客 开始 -->
                <div id="js_index_blog"></div>
                <!-- 博客 结束 -->
                <!-- 底部区轮播图 开始 -->
                <div ne-module="" class="index_foot_imgs" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
<div class="bottomnews_focus" ne-module="/modules/slide/slide.js" ne-state="slideMethod:left;events=mouseover;interval=3000;loop:1">
	<!--include virtual="/special/sp/mod_footer_img.html" -->
	<div class="bottomnews_box" ne-role="slide-body">
	<!-- 主要内容 648*402 20字-->
	<div class="bottomnews_scroll clearfix" ne-role="slide-scroll">
		<!-- 一页 -->
		<div class="bottomnews_main clearfix" ne-role="slide-page">
			<!-- 左 -->
						           			<div class="bottomnews_main_bimg bottomnews_main_img">
				<a href="http://news.163.com/photoview/00AO0001/2309353.html" target="_blank">
					<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-17/FHNMQGGR00AO0001NOS.jpg&thumbnail=839x2147483647&quality=75&type=jpg" width="100%">
				</a>
				<span class="bg"></span>
				<h2><a href="http://news.163.com/photoview/00AO0001/2309353.html" target="_blank">美国纽约州景点陆续向公众开放</a></h2>
			</div>
						<!-- 右 -->
			<div class="bottomnews_main_r">
				<div class="bottomnews_main_simgs clearfix">
										                   					<div class="bottomnews_main_simg bottomnews_main_img">
						<a href="http://news.163.com/photoview/00AN0001/2309341.html" target="_blank">
							<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-15/FHJUG5LO00AN0001NOS.jpg&thumbnail=359x2147483647&quality=75&type=jpg" width="100%" height="100%">
						</a>
						<span class="bg"></span>
						<h2><a href="http://news.163.com/photoview/00AN0001/2309341.html" target="_blank">安徽武警官兵和留守民众合力抢险</a></h2>
					</div>
										                   					<div class="bottomnews_main_simg bottomnews_main_img">
						<a href="http://news.163.com/photoview/00AP0001/2309372.html" target="_blank">
							<img ne-lazy="effect:fadeIn;slideIndex:0;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-18/FHQEOJUP00AP0001NOS.jpg&thumbnail=359x2147483647&quality=75&type=jpg" width="100%" height="100%">
						</a>
						<span class="bg"></span>
						<h2><a href="http://news.163.com/photoview/00AP0001/2309372.html" target="_blank">恩施启动城市防洪I级应急响应 城区多处被淹</a></h2>
					</div>
									</div>
			</div>
		</div>
		<!-- 一页 -->
		<div class="bottomnews_main clearfix" ne-role="slide-page">
			<!-- 左 -->
						           			<div class="bottomnews_main_bimg bottomnews_main_img">
				<a href="http://news.163.com/photoview/00AO0001/2309352.html" target="_blank">
					<img ne-lazy="effect:fadeIn;slideIndex:1;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-17/FHNJ93RL00AO0001NOS.jpg&thumbnail=839x2147483647&quality=75&type=jpg" width="100%">
				</a>
				<span class="bg"></span>
				<h2><a href="http://news.163.com/photoview/00AO0001/2309352.html" target="_blank">德国新冠确诊病例累计超20万例</a></h2>
			</div>
						<!-- 右 -->
			<div class="bottomnews_main_r">
				<div class="bottomnews_main_simgs clearfix">
										                   					<div class="bottomnews_main_simg bottomnews_main_img">
						<a href="http://news.163.com/photoview/00AN0001/2309333.html" target="_blank">
							<img ne-lazy="effect:fadeIn;slideIndex:1;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-15/FHILC0T900AN0001NOS.jpg&thumbnail=359x2147483647&quality=75&type=jpg" width="100%" height="100%">
						</a>
						<span class="bg"></span>
						<h2><a href="http://news.163.com/photoview/00AN0001/2309333.html" target="_blank">湖北黄梅小池镇长江干堤出现散浸</a></h2>
					</div>
										
										                   					<div class="bottomnews_main_simg bottomnews_main_img">
						<a href="http://news.163.com/photoview/00AP0001/2309364.html" target="_blank">
							<img ne-lazy="effect:fadeIn;slideIndex:1;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-17/FHP47HSR00AP0001NOS.jpg&thumbnail=359x2147483647&quality=75&type=jpg" width="100%" height="100%">
						</a>
						<span class="bg"></span>
						<h2><a href="http://news.163.com/photoview/00AP0001/2309364.html" target="_blank">长江重庆段水位持续上涨 临江商铺紧急转移</a></h2>
					</div>
									</div>
			</div>
		</div>
		<!-- 一页 -->
		<div class="bottomnews_main clearfix" ne-role="slide-page">
			<!-- 左 -->
						           			<div class="bottomnews_main_bimg bottomnews_main_img">
				<a href="http://news.163.com/photoview/00AO0001/2309351.html" target="_blank">
					<img ne-lazy="effect:fadeIn;slideIndex:2;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-16/FHM3VGAG00AO0001NOS.jpg&thumbnail=839x2147483647&quality=75&type=jpg" width="100%">
				</a>
				<span class="bg"></span>
				<h2><a href="http://news.163.com/photoview/00AO0001/2309351.html" target="_blank">佛州陷新冠危机 居民排长队接受检测</a></h2>
			</div>
						<!-- 右 -->
			<div class="bottomnews_main_r">
				<div class="bottomnews_main_simgs clearfix">
										                   					<div class="bottomnews_main_simg bottomnews_main_img">
						<a href="http://news.163.com/photoview/00AN0001/2309328.html" target="_blank">
							<img ne-lazy="effect:fadeIn;slideIndex:2;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-15/FHIHELSE00AN0001NOS.jpg&thumbnail=359x2147483647&quality=75&type=jpg" width="100%" height="100%">
						</a>
						<span class="bg"></span>
						<h2><a href="http://news.163.com/photoview/00AN0001/2309328.html" target="_blank">云南江城：全力消杀入侵蝗虫</a></h2>
					</div>
										
										                   					<div class="bottomnews_main_simg bottomnews_main_img">
						<a href="http://news.163.com/photoview/00AP0001/2309363.html" target="_blank">
							<img ne-lazy="effect:fadeIn;slideIndex:2;" data-original="http://nimg.ws.126.net/?url=https://pic-bucket.ws.126.net/photo/0001/2020-07-17/FHOURJG700AP0001NOS.jpg&thumbnail=359x2147483647&quality=75&type=jpg" width="100%" height="100%">
						</a>
						<span class="bg"></span>
						<h2><a href="http://news.163.com/photoview/00AP0001/2309363.html" target="_blank">航拍江水中的“万里长江第一阁”观音阁</a></h2>
					</div>
									</div>
			</div>
		</div>
		<!-- 结束 -->
	</div>
</div>
<a ne-role="slide-prev" class="bottomnews_focus_prev">&lt;</a>
<a ne-role="slide-next" class="bottomnews_focus_next">&gt;</a>
<div class="bottomnews_mask bottomnews_mask_l"></div>
<div class="bottomnews_mask bottomnews_mask_r"></div>
<div class="bottomnews_focus_title">
    <span ne-role="slide-nav" class="current">1</span>
    <span ne-role="slide-nav">2</span>
    <span ne-role="slide-nav">3</span>
</div>
	<!-- 结束 -->
</div></div>
                <!-- 底部区轮播图 结束 -->
                <!-- 通栏广告 开始 -->
                <div class="ns_area mt40 index_bottom_ad channel_relative_2016">
                    <!--16新闻首页底通-->
<div class="at_item common_ad_item bottom_ad_column" adType="bottomColumnAd" requestUrl="https://nex.163.com/q?app=7BE0FC82&c=news&l=12&site=netease&affiliate=news&cat=homepage&type=column1200x125_960x100browser&location=12"></div>
<span class="channel_ad_2016">广告</span>
                </div>
                <!-- 通栏广告 结束 -->
                <!-- 媒体合作 开始 -->
                <div class="ns_area index_media" ne-class="{{myState.isReadypage ? 'cm_area_show' : ''}}">
                    <h2>媒体合作</h2>
                    <ul class="clearfix">
	            <li class="first">
	                <div class="ns_media_box">
	                    <a href="http://www.xinhuanet.com/">新华网</a><a href="http://www.people.com.cn//">人民网</a><a href="http://www.chinanews.com/">中国新闻网</a><a href="http://www.chinadaily.com.cn/">中国日报网站</a><a href="http://www.cyol.com/">中青在线</a><a href="http://www.china.com.cn/">中国网</a><a href="http://www.youth.cn/">中国青年网</a><a href="http://gb.cri.cn/">国际在线</a><a href="http://www.taiwan.cn/">中国台湾网</a><a href="http://www.nddaily.com/">南方都市报</a><a href="http://www.bjnews.com.cn/">新京报</a><a href="http://www.jfdaily.com/">解放网</a><a href="http://www.eastday.com/">东方网</a><a href="http://www.ycwb.com/">金羊网</a><a href="http://www.cnhan.com/">汉网</a><a href="http://www.southcn.com/">南方网</a><a href="http://rednet.cn/">红网</a><a href="http://www.ynet.com/">北京青年报</a><a href="http://www.nen.com.cn/">东北新闻网</a><a href="http://www.dahe.cn/">大河网</a><a href="http://365jilin.com/">吉和网</a>
	                    <a class="" href="http://www.dzwww.com/">大众网</a><a class="" href="http://www.hsw.cn/">华商网</a><a class="" href="http://www.beijingdaily.com.cn/">北京日报</a><a class="" href="http://www.beijingdaily.com.cn/">北京晚报</a><a class="" href="http://www.dayoo.com/">大洋网</a><a class="" href="http://www.morningpost.com.cn/">北京晨报</a><a href="http://www.fznews.com.cn/">福州新闻网</a> 
	                </div>
	            </li>
	            <li class="second">
	                <div class="ns_media_box">
	                    <a href="http://www.cncnews.cn/">新华网络电视</a><a href="http://www.xdkb.net">现代快报</a><a href="http://www.3le.net.cn/xbsb/">西部商报</a><a href="http://qnck.cyol.com">青年参考</a><a href="http://www.ts.cn/">天山网</a><a href="http://www.jxnews.com.cn/">大江网</a><a href="http://www.ce.cn/">中国经济网</a><a href="http://www.hilizi.com/">半岛晨报</a><a href="http://www.cqwb.com.cn/">重庆晚报</a><a href="https://www.xxsb.com/">信息时报</a><a href="http://www.lzcbnews.com/">兰州晨报</a><a href="http://enews.xwh.cn">新文化报</a><a href="http://www.cctv.com">央视网</a><a href="http://www.hljnews.cn/">黑龙江新闻网</a><a href="http://www.cnhubei.com/">荆楚网</a><a href="http://war.163.com/special/00012ABP/junshifengmianxiugjzw.html">国际展望</a><a href="http://www.66wz.com/">温州网</a><a href="http://www.yndaily.com/">云南日报</a><a href="http://www.bbtnews.com.cn/">北京商报</a><a href="http://www.sznews.com/">深圳新闻网</a>
	                </div>
	            </li>
	            
	            <li class="third">
	                <div class="ns_media_box">
	                    <a href="http://www.northnews.cn">北方新闻网</a><a href="http://www.hebnews.cn">河北新闻网</a><a href="http://www.njnews.cn/">南京报业网</a><a href="http://www.sciencetimes.com.cn/">科学网</a><a href="http://www.huanqiu.com/">环球网</a><a href="http://www.xkb.com.cn/">新快网</a><a href="http://www.1news.cc/">长春日报</a><a href="http://www.voc.com.cn/">华声在线</a><a href="http://www.gmw.cn">光明网</a><a href="http://www.dbw.cn">东北网</a><a href="http://www.hinews.cn/">南海网</a><a href="http://www.kunming.cn/">昆明信息港</a><a href="http://www.ynxxb.com/">云信网</a><a href="http://www.e23.cn">舜网</a><a href="http://www.chinaweekly.cn">中国周刊</a><a href="http://www.changsha.cn/">星辰在线</a><a href="http://www.ybnews.cn/">延边新闻网</a><a href="http://www.iqilu.com/">齐鲁网</a>
	                    <a href="http://www.gettyimages.cn/">华盖创意</a>    
	                </div>
	            </li>
	            
	            <li class="last">
	                <div class="ns_media_box">
	                    <a href="http://www.dzwww.com/">大众网</a><a href="http://www.hsw.cn/">华商网</a><a href="http://www.fawan.com/">法制晚报</a><a href="http://www.scol.com.cn/">四川在线</a><a href="http://www.hebei.com.cn/">长城网</a><a href="http://www.godpp.gov.cn/">中国文明网</a><a href="http://www.daynews.com.cn/">山西新闻网</a><a href="http://www.yunnan.cn/ ">云南网</a><a href="http://www.jfdaily.com.cn/">解放日报</a><a href="http://www.nxnet.cn/">宁夏网</a><a href="http://www.chinatibetnews.com/">西藏新闻网</a><a href="http://www.qhnews.com/">青海新闻网</a><a href="http://www.hxfzzx.com/">海峡法治在线</a><a href="http://www.cankaoxiaoxi.com/">参考消息</a><a href="http://www.qx162.com">黔讯网</a><a href="http://news.iyaxin.com/">亚心网</a><a href="http://www.tibet.cn/">中国西藏网</a>
	                </div>
	            </li>
	        </ul>
                </div>
                <!-- 媒体合作 结束 -->
                <div class="ns_area foot_execute_leader">执行主编：黄欢_NN1650</div>
                <!-- 底部 开始 -->
                <style type="text/css" _keep="true">
        /* footer */
        .ft_icons{background-image:url(http://static.ws.126.net/f2e/news/index2016_rmd/images/sprite_foot20181010.png);}
        .index_footer{border-top:1px solid #ddd;height:270px;background:#f8f8f8;margin-top:20px;}
        .ns_pot_bar {width:240px;padding-top:50px;float:right;margin-right: 35px;}
        .ns_pot_logo {width:220px;height:270px;border-right:1px solid #ddd;float:left;}
        .ns_pot_news {width:240px;height:270px;border-right:1px solid #ddd;float:left;}
        .ns_pot_site {width:420px;height:270px;border-right:1px solid #ddd;float:left;}
        .ic_news_ft{display:block;margin-top: 20px;width: 142px;height: 65px;background-position: 0px -200px;}
        .ns_pot_news h4,.ns_pot_site h4{padding:30px 0 10px 30px;color:#808080;font-weight:bold}
        .ns_pot_news li,.ns_pot_site li{float:left;width:70px;padding:0 0 10px 30px;}
        .ns_pot_news p,.ns_pot_site p{padding-left:30px;}
        .ns_pot_news a,.ns_pot_site a{color: #888;}
        .ns_pot_news a:hover,.ns_pot_site a:hover{color: #ba2636;}
        .ns-pot-share a{float:left;margin-right:10px;}
        .ns-pot-history {position: relative;height: 27px; width: 110px;margin: 30px 0 0 25px;color: #888;cursor:pointer;}
        .ns-pot-history .ns-calendar {position: absolute;bottom:36px;left:0;z-index:99;}
        .ns-pot-tri {height: 25px; width: 100px; line-height: 26px;border:1px solid #ddd;padding-left: 8px;background:#fff;position:relative;}
        .ns-pot-tri i{position:absolute;right:10px;top:9px;z-index:3;overflow:hidden;}
        .ns-pot-tri:hover i{background-position: 0 -859px;}
        .ns_pot_search {height: 28px; width: 225px; line-height: 26px;border:1px solid #ddd;padding-left: 8px;background:#fff;position:relative;margin: 30px 0 0 0px;overflow:hidden;}
        .ns_pot_search .search_texh {height:28px;width:200px;border:0;margin:0;color: #888;line-height:28px;}
        .ns_pot_search .search_btn{border:0;padding:0;position: absolute;right:10px;top:6px;text-indent:100px;overflow:hidden;z-index:3;width:24px;height:24px;background-position:-117px -4px;background-color:#fff;}
        .ic_lofter_ft,.ic_mail_ft,.ic_rss_ft {width:33px;height:33px;transition: background 0.3s cubic-bezier(.17, .67, .88, 1.25);}
        .ic_lofter_ft{background-position: 0 -1px;}
        .ic_lofter_ft:hover{background-position: 0 -34px;}
        .ic_mail_ft{background-position: 0 -67px;}
        .ic_mail_ft:hover{background-position: 0 -100px;}
        .ic_rss_ft{background-position: 0 -133px;}
        .ic_rss_ft:hover{background-position: 0 -166px;}
        .ic_newsapp_ft{float:left;_display:inline;width: 26px;height: 30px;border-left: 1px solid #cbcbcb;padding-left: 16px;margin-left: 10px;}
        .ic_newsapp_ft a{margin-right:0;display: block;width: 26px;height: 30px;background:url(http://static.ws.126.net/f2e/news/index2015/img/newsapp.png) no-repeat;_background:url(http://img1.cache.netease.com/f2e/news/index2015/img/newsapp_8.png) no-repeat;background-position: 0 0;-webkit-transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);-moz-transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);-o-transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);}
        .ic_newsapp_ft a:hover{background-position: 0 -31px;}
        .ic_cloudapp_ft{float:left;width: 33px;height: 33px;margin-right: 10px;background:url(http://static.ws.126.net/f2e/news/res/img/cloudapp.png) no-repeat;_background:url(http://static.ws.126.net/f2e/news/res/img/cloudapp_8.png) no-repeat;background-position: 0 0;-webkit-transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);-moz-transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);-o-transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);transition:background 0.3s cubic-bezier(.17, .67, .88, 1.25);}
        .ic_cloudapp_ft:hover{background-position: 0 -34px;}
        .ns9 .ns_pot_logo {width:150px;}
        .ns9 .ns_pot_news {width:190px;}
        .ns9 .ns_pot_site {width:300px;}
        .ns9 .ns_pot_news li,.ns9 .ns_pot_site li{width:50px;padding-left: 30px;}
        .ns9 .ns_pot_news h4,.ns9 .ns_pot_site h4{padding-left: 30px;}
        .ns9 .ns_pot_news p{padding-left:30px;}
        .ns9 .ns_pot_site{width: 360px;}
        .ns9 .ns_pot_bar{margin-right: 0;}
        </style>
	    <div class="index_footer">
		    <div class="ns_area clearfix">
		        <div class="ns_pot_logo"><a href="http://3g.163.com/links/6691"><i class="ft_icons ic_news_ft"></i></a></div>    
		            
		        <div class="ns_pot_news">
		            <h4>新闻</h4>
		            <ul class="clearfix">
		                <li><a href="http://news.163.com/domestic/">国内</a></li>
		                <li><a href="http://news.163.com/world/">国际</a></li>
		                <li><a href="http://news.163.com/photo/">图片</a></li>
		                <li><a href="http://news.163.com/air/">航空</a></li>
		                <li><a href="http://war.163.com/">军事</a></li>
		                <li><a href="http://news.163.com/rank/">排行</a></li>
		            </ul>
		            <p><a href="http://news.163.com/review/">新闻地图&gt;&gt;</a></p>
		        </div> 
		               
		        <div class="ns_pot_site">
		            <h4>其他频道</h4>
		            <ul class="clearfix">
		                <li><a href="http://sports.163.com/">体育</a></li>
		                <li><a href="http://tech.163.com/">科技</a></li>
		                <li><a href="http://v.163.com/">视频</a></li>
		                <li><a href="http://edu.163.com/">教育</a></li>
		                <li><a href="http://ent.163.com/">娱乐</a></li>
		                <li><a href="http://mobile.163.com/">手机</a></li>
		                <li><a href="http://www.lofter.com/?act=qb163rk_20141031_03">LOFTER</a></li>
		                <li><a href="http://book.163.com/">读书</a></li>
		                <li><a href="http://money.163.com/">财经</a></li>
		                <li><a href="http://digi.163.com/">数码</a></li>
		                <li><a href="http://book.163.com/art">艺术</a></li>
		                <li><a href="http://money.163.com/stock/">股票</a></li>
		                <li><a href="http://auto.163.com/">汽车</a></li>
		                <li><a href="http://play.163.com/">游戏</a></li>
		                <li><a href="http://lady.163.com/">女人</a></li>
		                <li><a href="http://house.163.com/">房产</a></li>
		                <li><a href="http://travel.163.com/">旅游</a></li>
		                <li><a href="http://m.163.com/">应用</a></li>
		                <li><a href="http://gov.163.com/">政务</a></li>
		                <li><a href="http://study.163.com/?utm_source=news.163.com&utm_medium=web_bottomnav&utm_campaign=business">云课堂</a></li>
		                <li><a href=" http://jiankang.163.com">健康</a></li>
		            </ul>
		        </div>   
		             
		        <div class="ns_pot_bar">
		            <div class="ns-pot-share clearfix">
		                <a class="ft_icons ic_lofter_ft" href="http://www.lofter.com/?act=qb163rk_20141031_03"></a>
		                <a class="ft_icons ic_mail_ft" href="http://email.163.com/"></a>
		                
						<a href="http://study.163.com/?utm_source=163.com&utm_medium=web_bottomlogo&utm_campaign=business" class="ic_cloudapp_ft"></a>
						<div class="ic_newsapp_ft">
						    <a href="http://www.163.com/newsapp/#f=down" class="ft_icons"></a>
						</div>
				    </div>
		            
		            <div class="ns_pot_search">
		                <form action="http://news.yodao.com/search" method="get">         
		                    <input class="search_texh" type="text" name="q" autocomplete="off" value="输入关键字">
		                    <input class="ft_icons search_btn" type="submit" value="搜索">
		                    <input type="hidden" name="keyfrom" value="news.163">
		                    <input type="hidden" name="suser" value="user163">
		                    <input type="hidden" name="ue" value="gbk">
		                    <input type="hidden" name="site" value="网易">
		                    <input type="hidden" name="in" value="page">
		                </form>
		            </div>        
		        </div>
		    </div>      
		</div>
                <!-- 底部 结束 -->
                <!-- 加载多个nex合并一个请求的广告 -->
                <div id="loadlazynex" class="hidden" _nexurl="https://static.ws.126.net/163/f2e/modules/adtracker2019/js/foot~285d3eeda83af.js"></div>
            </div>
        </div>
    </div>
    <!-- 二维码 -->
    <div class="ns_sidebar none">
        <a href="http://news.163.com/16/0602/16/BOIMS8PF00014JB5.html " target="_blank" class="ic_guide">新版<br/>反馈</a>
        <div class="ns_side_qrcode"><i class="ft_icons ic_qrcode"></i></div>
        <div class="ns_side_tolid"><i class="ft_icons ic_totop"></i></div>
    </div>
    <div class="N-nav-bottom">
    <div class="N-nav-bottom-main">
        <div class="ntes_foot_link">
            <span class="N-nav-bottom-copyright"><span class="N-nav-bottom-copyright-icon">&copy;</span> 1997-2020 网易公司版权所有</span>
            <a href="http://corp.163.com/">About NetEase</a> |
            <a href="http://gb.corp.163.com/gb/about/overview.html">公司简介</a> |
            <a href="http://gb.corp.163.com/gb/contactus.html">联系方法</a> |
            <a href="http://corp.163.com/gb/job/job.html">招聘信息</a> |
            <a href="http://help.163.com/ ">客户服务</a> |
            <a href="http://gb.corp.163.com/gb/legal.html">隐私政策</a> |
            <a href="http://emarketing.163.com/">广告服务</a> |
           <!--  <a ne-role="feedBackLink" ne-click="handleFeedBackLinkClick()" href="http://www.163.com/special/0077450P/feedback_window.html" class="ne_foot_feedback_link">意见反馈</a> | -->
            <a href="http://jubao.aq.163.com/">不良信息举报 Complaint Center</a> |
            <a href="https://jubao.163.com/">廉正举报</a>
        </div>
    </div>
</div>
</div>
<!-- 节日背景 -->
<!-- <script src="//house.163.com/special/0007rt/ipauto.js" charset="gbk" _keep="true"></script> -->
<!-- 社交传播统计 -->
<script src="//static.ws.126.net/163/frontend/libs/antanalysis.min.js"></script>
<script src="//static.ws.126.net/163/frontend/antnest/NTM-KFGT6I8U-38.js" _keep="true"></script>
<script src="https://static.ws.126.net/163/frontend/libs/raven-3.26.2.min.js" crossorigin="anonymous"></script>
<script _keep="true">
Raven.config("https://91aeb483c19a44cbb9bf11a8b0a5e6eb@sentry.music.163.com/97",{
    ignoreErrors:[
        "i is not a function",
        "'null' is not a function",
        "console",
        "undefined",
        "platform",
        "neteaseTracker",
        "JSON input",
        "Object expected",
        "Exception invoking getOffsetHeight",
        "Unexpected token o in JSON at position",
        "nadScreenFloat",
        "toString",
        "Syntax error",
        "unexpected character",
        "Unexpected token l in JSON at position 0",
        "onLayoutChanged is not defined",
        "Exception invoking getBoundingClientRect",
        "Exception invoking getClientHeight",
        "Exception invoking getOffsetTop",
        "Exception invoking getScrollHeight",
        "Argument not optional",
        "Invalid character",
        "n.URS is not a constructor",
        "Object doesn't support this action",
        "Cannot read property 'tagName' of null",
        "$ is not defined",
        "Unexpected identifier",
        "JSON at position",
        "onLoginStatusChanged",
        "errorx5onSkinSwitch",
        "Cannot redefine non-configurable property 'width'",
        "width"
    ]
}).install()
</script>
<!-- <script src="//news.163.com/special/00015CJL/xw_news_data.js" charset="gbk" _keep="true"></script> -->
<script type="text/javascript" _keep="true">
(function() {
    //广告判断使用
    var isNs9 = false;
    var winWidth = window.innerWidth || document.documentElement.clientWidth;
    if(winWidth < 1360 || /\?narrow/.test(location.search)) {
        isNs9 = true;
    }
    window.isNs9 = isNs9;
})();
</script>
<!-- 2020-07-18 14:31:35 -->
<!--!include collector="foot"-->
<script src="https://static.ws.126.net/163/f2e/news/index2016_rmd/js/foot~8d33f64fc6836.js" async="async"></script>
<!-- 公共尾部引用 -->

<!--  -->
<!-- 章鱼统计 -->

<!-- STAT WRating v1.0 -->
<!-- STAT NetEase Devilfish 2006 -->
<script type="text/javascript" src="//analytics.163.com/ntes.js"></script>
<script type="text/javascript">
    _ntes_nacc = "news"; //站点ID。
    try {
                if(typeof neteaseTracker === "function") { 
                    neteaseTracker();
                } else { 
                   
                }
  } catch(e) {}
</script>
<!-- big data statistics -->

<!-- big data analysis 0628 -->
<script src="https://static.ws.126.net/f2e/products/analysis/js/analysis0628.350ctAoOoFtN.1.js"></script>
<!-- 360广告 -->
<script src="//static.ws.126.net/163/f2e/modules/netsposter/js/netsposter2019_main-9af9104974.js"></script>

<!-- 富媒体广告 begin --> 
<!-- 广告位：网易右下角视窗开始 -->
<div id="ssp_6502161"></div>
<script>
(function() {
	(window.slotbydup=window.slotbydup || []).push({
		id: '6502161',
		container: 'ssp_6502161',
		size: '320,240',
		display: 'inlay-fix',
		async:true
	});
})();
</script>
<!--<script async defer src="https://dup.baidustatic.com/js/os.js"></script> -->
<!-- 广告位：网易右下角视窗结束 -->
<!-- 浮层 -->
<SCRIPT LANGUAGE="JavaScript1.1" src="https://g.163.com/jr?site=netease&affiliate=news&cat=homepage&type=richmedia&location=1"></SCRIPT>
<!-- 角标样式 勿删-->
<style type="text/css">
 .ad_hover_href {
  width: 30px;
  height: 17px;
  position:absolute;
  left:0;
  bottom:0;
  z-index:10;
  background:url(https://yt-adp.ws.126.net/channel4/ad_3017_ajgf_20190221.png) no-repeat;
 }
</style>
<!-- 角标样式 勿删-->
<div id="ssid1"></div>
<!--对联有广告定向-->
<SCRIPT LANGUAGE="JavaScript1.1" src="https://g.163.com/jr?site=netease&affiliate=news&cat=homepage&type=richmedia&location=2"></SCRIPT>
<!--对联有广告开始-->
<!-- <script>
var coupletTop = 100;
var coupletLeftHref="http://g.163.com/a?CID=75916&Values=2183505036&Redirect=https://e.cn.miaozhen.com/r/k=2163047&p=7Yy98&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&m11=__OAID__&mn=__ANAME__&o=";
var coupletRightHref="http://g.163.com/a?CID=75916&Values=2183505036&Redirect=https://e.cn.miaozhen.com/r/k=2163047&p=7Yy98&dx=__IPDX__&rt=2&ns=__IP__&ni=__IESID__&v=__LOC__&xa=__ADPLATFORM__&tr=__REQUESTID__&ro=sm&mo=__OS__&m0=__OPENUDID__&m0a=__DUID__&m1=__ANDROIDID1__&m1a=__ANDROIDID__&m2=__IMEI__&m4=__AAID__&m5=__IDFA__&m6=__MAC1__&m6a=__MAC__&m11=__OAID__&mn=__ANAME__&o=";
var coupletLeftUrl = 'https://yt-adp.ws.126.net/channel21/041630_20300_aklm_20200407.jpg';
var coupletRightUrl ='https://yt-adp.ws.126.net/channel21/041630_20300_aklm_20200407.jpg';
var coupletLeftUrlb = 'https://yt-adp.ws.126.net/channel21/041630_bvlo_20200407.swf';
var coupletRightUrlb = 'https://yt-adp.ws.126.net/channel21/041630_bvlo_20200407.swf';
</script> 
<script src="https://yt-adp.ws.126.net/ntesrich/auto/js/news_dl_2015.11.18.js"></script> -->
<!--对联有广告结束-->
<!-- 流媒体 begin -->  
<!-- <script type="text/javascript" src="http://popme.163.com/js/nadTimeFlashLayer3.js"></script>
<script type="text/javascript">//<![CDATA[
new nadFlashLayer(
'http://img1.126.net/channel4/013525/200150_0131a.swf',
'nad2234Home',{
//nextId:'nad2234Home1',
visibility:true,
time:5,
xPx:-100,
yPx:400
});
new nadFlashLayer(
'http://img1.126.net/channel4/012437/yili200150_0831.swf',
'nad2234Home1',{
nextId:'',
visibility:false,
time:5,
xPx:-100,
yPx:450
});
//></script> -->
<!-- 流媒体 end -->
<!-- 全屏收缩 begin -->
<!-- <script type="text/javascript" src="https://yt-adp.ws.126.net/myzhang/test/nadScreenFloat2011_1.js"></script>
<script type="text/javascript" src="https://yt-adp.ws.126.net/myzhang/test/nadTimeFlashLayer3.js"></script>
<script type="text/javascript">//<![CDATA[
new nadScreenFloat("https://yt-adp.ws.126.net/channel14/039256_750550_acra_20190926.jpg",{
type		:	"image",
href		:	"http://g.163.com/a?CID=72368&Values=3380557273&Redirect=http://www.changan-mazda.com.cn/product/mazda3/",
playFunc	:	function(){
new nadFlashLayer(
'',
'nad2234Home',{
//nextId:'nad2234Home1',
visibility:true,
time:5,
xPx:-100,
yPx:400
});
new nadFlashLayer(
'http://img1.126.net/channel4/012437/yili200150_0831.swf',
'nad2234Home1',{
nextId:'',
visibility:false,
time:8,
xPx:-100,
yPx:450 
});
}
});
//]]></script> -->
<!-- 尺寸适配 -->
<script type="text/javascript">
(function() {
    isNs9 = false;
    if(window.innerWidth <1366) {
        isNs9 = true;
    }
    window.isNs9 = isNs9;
})();
</script>
<!--弹窗代码-->
<SCRIPT LANGUAGE="JavaScript1.1" class="cmbaidu_js_ad" _src="https://g.163.com/r?site=netease&affiliate=news&cat=homepage&type=popwin&location=1"></SCRIPT>
<SCRIPT LANGUAGE="JavaScript1.1" class="cmbaidu_js_ad" _src="https://g.163.com/jr?site=netease&affiliate=news&cat=homepage&type=popup&location=1 "></SCRIPT>
<!--广告顺序管理开始-->
<script language="javascript" src="https://img3.126.net/ntesrich/auto/adbox/adbox-v1.1.2-120705.js"></script>
<script language="javascript"  class="cmbaidu_js_ad" _src="https://img3.126.net/ntesrich/2013/1210/adControl-indexx-v1.0.2-131210.js"></script>
<!--广告顺序管理结束-->
<!--special/sp/test_news_db_16.html-->
<!-- 富媒体广告 end --> 
<!-- 统计 -->
<script>!function(i){function e(){}function n(){var i=Math.round((+new Date-A)/1e3);return i<0?0:i}function t(i){var e=i.className,n=r(i),t={script:1,style:1,link:1,img:1,hr:1,br:1},a=!0;return t[n]?a=!1:/blank\d/.test(e)&&(a=!1),a}function a(e){b||(h&&window._ntes_sendInfo?(i.each(x,function(i,e){f(i)}),b=!0):x.push(e)),b&&f(e)}function o(i){return i<10?i.toString():i>62?"z":String.fromCharCode(i+(i<36?55:61))}function l(i,e){if(!e)return i;var n=i.length-1,t=i.charCodeAt(n);return t<58?t-=48:t<91?t-=55:t<123&&(t-=61),i.substr(0,n)+o(t+e)}function s(i,e,n){e&&e.setAttribute((n?"_":"")+"jcid",i)}function c(i){if(i){var e=this.getAttribute("href")||"";w++;var t="/ntes_p?"+g+"&_nct="+n()+"&_nah="+escape(e)+"&_nat={id}_"+i;a(t)}}function f(i){_ntes_sendInfo("jc",_ntes_src_addr+i.replace("{id}",h))}function _(i,e,n){for(var t={a:1,area:1},a=i,o=null;i.tagName&&i!=y;){if(t[r(i)]){o=i;break}i=i.parentNode}if(o)for(;i&&i!=e&&!(n=i.getAttribute("jcid"));)i=i.parentNode;for(;!n&&!(n=a.getAttribute("_jcid"));)if(a=a.parentNode,!a||!a.tagName||a==y)return;n&&c.call(o||i,n)}function r(i){return i.tagName.toLowerCase()}function d(i){return(i.innerHTML.match(/jcid=".*?"/g)||[]).join("")}function u(e,n){var t,a;i(e).bind("mouseover touchstart",function(){var i=d(e),o=e.innerHTML.replace(/<.*?>/g,"").length;!e.children.length||i==t&&o==a||(n(),t=d(e),a=o)})}function m(i,e){var n=i[0],t=i.level;return n&&t&&v(n,t,e),n}function v(e,n,t){if(i.isArray(e))i.each(e,function(i,e){v(i,n,t)});else if("object"==typeof e)if(e.i)e.k=l(e.i.substr(0,n+1),t)+e.i.substr(n+1);else for(var a in e)v(e[a],n,t)}var h,p,g="_nacc=siteclick&_npurl="+escape(document.URL),w=0,b=!1,x=[],y=document.body,A=window.performance&&window.performance.timing?window.performance.timing.connectStart:+new Date,j=[function(e,n,t){e+=o(t.start||1),t.bind?i(n).bind("click",function(i){c.call(n,e)}):s(e,n,t.all)},function(e,n,t){var a,l=t.start||1,c=t.query||"a";/(.*?)\|(.*)/.test(c)?(a=RegExp.$1,c=RegExp.$2,i(a,n).each(function(n,a){l=t.start||1,i(c,n).each(function(i,n){s(e+o(l++),i,t.all)})})):i(c,n).each(function(i,n){s(e+o(l++),i,t.all)})},function(e,n,a){for(var l=1,c=a.level||1,f=[n],_=0;_<c;_++){var d=[];i.each(f,function(e,n){var a=0;"a"==r(e)||/ntes-nav-select/.test(e.className)||i.each(e.children,function(i,e){t(i)&&(d.push(i),a++)}),a||d.push(e)}),f=d}i.each(f,function(i,n){s(e+o(l++),i,a.all)})},function(e,n,t){var a=i(">form",n);a[0]&&a.bind("submit",function(){c.call(this,e+"1")})},function(e,n,t){var a=i(t.h,n),l=i(t.b,n);if(a&&l){var c=t.step||10,f=2;s(e+"1",n),a.each(function(i,n){s(e+o(f+n*c),i)}),l.each(function(i,n){s(e+o(f+n*c+1),i)})}},function(e,n,a){var l=a.union||"",c={};if(/^[\s\d,]+$/.test(l)){var f=0;i.each(l.split(/\s*,\s*/),function(i,e){if(i=parseInt(i))for(var n=0;n<i;n++)c[f++]=e})}var _=2;s(e+"1",n);var r=parseInt(a.step)||10,d=i(a.h,n);if(d&&u){i.each(d,function(i,n){s(e+o(n*r+_),i)});var u=i(a.b,n);i.each(u,function(n,a){var l=a*r+_+1,f=n.children;if(0==f.length)f=[n];else for(;1==f.length;)f=f[0].children;var d=0;i.each(f,function(i,n){t(i)&&("undefined"!=typeof c[n]&&(d=c[n]),s(e+o(l+d),i),d++)})})}}];e.prototype={init:function(e,t){e&&5==e.length&&(h=e),p||(p=location.href.indexOf("_aCM")>-1||Math.random()<(t||.1),p&&(i("body").bind("click",function(i){_(i.target,y)}),i(function(){function e(){o&&(a("/ntes_u?"+o+"&_nct="+n()+"&_mcn="+w+l),o=0)}var t=i(window),o=g+"&_nch={id}",l="",s="&_msl="+n();t.bind("load",function(){l="&_msl="+n()}),a("/ntes_u?"+o+s),t.bind("beforeunload",e);var c=navigator.userAgent.toLowerCase();!/compatible/.test(c)&&/firefox/.test(c)&&t.bind("unload",e)}),this.retain&&this.area(y,this.retain)))},area:function(i,e,n){for(var t in e){var a=!1,o=e[t];o.level=n||0,/(.*?)=$/.test(t)&&(t=RegExp.$1,a=!0),this.procA(i,t,o,a)}},procA:function(e,n,t,a){var o=this,l=t.level+1;if(a)return void u(e,function(){o.procA(e,n,t)});var s=function(i,e){o.area(i,e,l)},c=0,f=0,_=0;/(.*?)!$/.test(n)&&(n=RegExp.$1,f=1),/(.*?)\*$/.test(n)?(n=RegExp.$1,c=1):/(.*?)\+$/.test(n)&&(n=RegExp.$1,_=1);var r,d=n?i(n,e):[e],v=0,h=d.length;for(r=0;r<h;r++){var p=d[r];if(!f||!p.id){var g=c?t[0]:t[v];if(_&&1==t.length&&(g=m(t,v)),g&&p)if(g.i)for(var w=g.s||1,b=0;b<w;b++)g.j=b,this.zone(d[r+b],g);else s(p,g);v++}}},zone:function(i,e){var n=l(e.k||e.i,e.j),t=j[e.f||0],a=e.p||{};i&&t&&(a.dyn?u(i,function(){t(n,i,a)}):t(n,i,a))},batch:function(i){p?this.area(y,i):this.retain=i}},window._aCM=new e}(window.bowlder),function(){_aCM.init(window._aCMID||"xwa01"),setTimeout(function(){_aCM.batch({".ntes-nav-main":[{".ntes-nav-app":[{"":[{i:"111",f:1}]}],".ntes-nav-entry-wide":[{"":[{i:"121"}]}],".c-fl":[0,0,0,0,{".ntes-nav-login-title":[{i:"131"}],">.ntes-nav-select":[{i:"132",f:1}]},0,{"*#js_login_suggest_wrap":[{i:"141",f:1}],"#js_N_navLogout":[{i:"142"}]}],".ntes-nav-inside>li":[{">.ntes-nav-select":[{i:"151",f:1}]},{">.ntes-nav-select":[{i:"161",f:1}]},{">.ntes-nav-select":[{i:"171",f:1}]},{">.ntes-nav-select":[{i:"181",f:1}]},{">.ntes-nav-select":[{i:"191",f:1}]},{">.ntes-nav-select":[{i:"1A1",f:1}]},{">.ntes-nav-select":[{i:"1B1",f:1}]},{">.ntes-nav-select":[{i:"1C1",f:1}]},{">.ntes-nav-select":[{i:"1D1",f:1}]}]}],".N-nav-channel":[{"":[{"":[{i:"211",f:1}]}]}],".index_top_ad":[{"":[{"":[{i:"311"}]}]}],".index_head":[{h1:[{"":[{i:"411"}]}],".top-search":[{"":[{i:"421",f:3}]}],"#nsWeather":[{"":[{i:"431"}]}],".first":[{"":[{i:"441"}]}],li:[0,{"":[{i:"451"}]},{"":[{i:"461"}]},0,0,0,{"":[{i:"4A1"}]},{"":[{i:"4B1"}]},0,0,0,{"":[{i:"4F1"}]},{"":[{i:"4G1"}]},{"":[{i:"4H1"}]}],".menu_guonei":[{"":[{i:"471"}]}],".menu_guoji":[{"":[{i:"481"}]}],".menu_shehui":[{"":[{i:"491"}]}],".menu_war":[{"":[{i:"4C1"}]}],".menu_hangkong":[{"":[{i:"4D1"}]}],".menu_wurenji":[{"":[{i:"4E1"}]}],".last":[{"":[{i:"4I1"}]}]}],".index_main":[{".origina_column_warp":[{".cell_hs":[{i:"511",f:1}],".cell_sd":[{i:"512",f:1}],".cell_rj":[{i:"513",f:1}],".cell_dgxm":[{i:"514",f:1}],".cell_dada":[{i:"515",f:1}],".cell_qsyk":[{i:"516",f:1}],".cell_caozhi":[{i:"517",f:1}],".cell_zajia":[{i:"518",f:1}],".cell_kanke":[{i:"519",f:1}],".cell_hotsee":[{i:"51A",f:1}],".cell_yuandian":[{i:"51B",f:1}],".ne-scrl-ct":[{i:"51C"}]}],"#js_top_news":[{">h2":[{i:"521"}],li:[{i:"522"},{i:"523"},{i:"524"},{i:"526"},{i:"527"},{i:"528"}],">.top_news_title":[{i:"525"}]}],".mod_top_news_ad":[{"":[{i:"531"}]}],".mod_important_news":[{">h2":[{i:"541"}],li:[{i:"542",s:5}]}],".mod_idx_focus":[{h2:[{i:"551"}],">.focus_prev":[{i:"552"}],">.focus_next":[{i:"553"}],li:[{i:"554",f:1,s:4}]}],".newsdata_wrap":[{">.newsdata_nav":[{i:"561",f:1,p:{dyn:1}}],">.newsdata_prev":[{i:"562"}],">.newsdata_next":[{i:"563"}],".newsdata_item":[{i:"564",f:2,p:{level:2,dyn:1}},{i:"565",f:2,p:{level:2,dyn:1}},{i:"566",f:2,p:{level:2,dyn:1}},{i:"567",f:2,p:{level:2,dyn:1}},{i:"568",f:2,p:{level:2,dyn:1}},{i:"569",f:2,p:{level:2,dyn:1}},{i:"56A",f:2,p:{level:2,dyn:1}},{i:"56B",f:2,p:{level:2,dyn:1}},{i:"56C",f:2,p:{level:2,dyn:1}},{i:"56D",f:2,p:{level:2,dyn:1}},{i:"56E",f:2,p:{level:2,dyn:1}},{i:"56F",f:2,p:{level:2,dyn:1}},{i:"56G",f:2,p:{level:2,dyn:1}},{i:"56H",f:2,p:{level:2,dyn:1}},{i:"56I",f:2,p:{level:2,dyn:1}},{i:"56J",f:2,p:{level:2,dyn:1}},{i:"56K",f:2,p:{level:2,dyn:1}}],">.load_more_btn":[{i:"56L"}]}],".mod_right_focus>div!":[{li:[{i:"571",s:4}],".f_prev":[{i:"575"}],".f_next":[{i:"576"}]}],".mod_ad_toutu":[{li:[{i:"581",s:4}]}],">.main_right_channel>div>div!":[0,{".cell_hs":[{i:"591",f:1}],".cell_sd":[{i:"592",f:1}],".cell_rj":[{i:"593",f:1}],".cell_dgxm":[{i:"594",f:1}],".cell_dada":[{i:"595",f:1}],".cell_qsyk":[{i:"596",f:1}],".cell_caozhi":[{i:"597",f:1}],".cell_zajia":[{i:"598",f:1}],".cell_kanke":[{i:"599",f:1}],".cell_hotsee":[{i:"59A",f:1}],".cell_yuandian":[{i:"59B",f:1}],".ne-scrl-ct":[{i:"59C"}]}],".mt12>div!":[{"":[{i:"5A1"}]}],".mod_pageh5>div!":[{">.idx_cm_title":[{i:"5B1"}],".h5_item_poster":[{i:"5B2",s:4}],".scrollbtl":[{i:"5B6"}],".scrollbtnr":[{i:"5B7"}]}],".mt30":[{".title":[{i:"5C1"}],".photo":[{i:"5C2"}],strong:[{i:"5C3"}],li:[{i:"5C4",s:4}]}],".mod_high_dynamic":[{".title":[{i:"5D1"}],li:[{i:"5D2",s:2}]}],".mt25>div!":[{"":[{i:"5E1"}]},{"":[{i:"5I1"}]},0,0,{"":[{i:"5O1"}]}],".mod_war":[{".title":[{i:"5F1"}],">.idx_cm_img":[{i:"5F2"}],li:[{i:"5F3",s:4}]}],".mod_ad_r>div!":[0,0,{"":[{i:"5G1"}]},0,{"":[{i:"5L1"}]},0,{"":[{i:"5Q1"}]},{"":[{i:"5U1"}]},{"":[{i:"5Y1"}]}],".mod_hot_rank":[{">.idx_cm_title":[{i:"5H1"}],".top":[{i:"5H2",s:3}],li:[0,0,0,{i:"5H5"},{i:"5H6"},{i:"5H7"},{i:"5H8"},{i:"5H9"},{i:"5HA"},{i:"5HB"}]}],".mod_money":[{".title":[{i:"5J1"}],">.idx_cm_img":[{i:"5J2"}],li:[{i:"5J3",s:4}]}],".mod_sports":[{".title":[{i:"5K1"}],">.idx_cm_img":[{i:"5K2"}],li:[{i:"5K3",s:4}]}],".mod_ent":[{".title":[{i:"5M1"}],">.idx_cm_img":[{i:"5M2"}],li:[{i:"5M3",s:4}]}],".mod_auto":[{".title":[{i:"5N1"}],">.idx_cm_img":[{i:"5N2"}],li:[{i:"5N3",s:4}]}],".mod_house":[{">.idx_cm_title":[{i:"5P1",f:1}],">.idx_cm_img":[{i:"5P2"}],li:[{i:"5P3",s:4}]}],".mod_wonderful_video":[{">.idx_cm_title":[{i:"5R1"}],">.big_video":[{i:"5R2"}],">.small_video":[{i:"5R3",f:1}]}],".mod_tech":[{".title":[{i:"5S1"}],">.idx_cm_img":[{i:"5S2"}],li:[{i:"5S3",s:4}]}],".mod_digi":[{".title":[{i:"5T1"}],">.idx_cm_img":[{i:"5T2"}],li:[{i:"5T3",s:4}]}],".mod_lady":[{".title":[{i:"5V1"}],">.idx_cm_img":[{i:"5V2"}],li:[{i:"5V3",s:4}]}],".mod_edu":[{".title":[{i:"5W1"}],">.idx_cm_img":[{i:"5W2"}],li:[{i:"5W3",s:4}]}],".mod_jiankang":[{".title":[{i:"5X1"}],">.idx_cm_img":[{i:"5X2"}],li:[{i:"5X3",s:4}]}],".mod_bobo":[{".title":[{i:"5Z1"}],li:[{i:"5Z2",f:1,s:7}]}],".mt13>div!":[{"":[{i:"5a1"}]}]}],"#js_index_blog":[{">.hd":[{"":[{i:"611",f:1}]}],".blog_con":[{"":[{i:"621",f:1}]},{"":[{i:"631",f:1}]},{"":[{i:"641",f:1}]},{"":[{i:"651",f:1}]}]}],".bottomnews_focus":[{".bottomnews_main_bimg":[{"":[{i:"711",f:2}]},{"":[{i:"731",f:2}]},{"":[{i:"751",f:2}]}],".bottomnews_main_simgs":[{">.bottomnews_main_simg":[{i:"721",f:2,s:2}]},{">.bottomnews_main_simg":[{i:"741",f:2,s:2}]},{">.bottomnews_main_simg":[{i:"761",f:2,s:2}]}],">.bottomnews_focus_prev":[{"":[{i:"771"}]}],">.bottomnews_focus_next":[{"":[{i:"781"}]}]}],".mt40":[{"":[{"":[{i:"811"}]}]}],".index_media":[{".ns_media_box":[{"":[{i:"911",f:1}]},{"":[{i:"921",f:1}]},{"":[{i:"931",f:1}]},{"":[{i:"941",f:1}]}]}],".ns_area":[0,0,0,0,0,0,0,0,{">.ns_pot_logo":[{"":[{i:"A11"}]}],ul:[{">li":[{i:"A21",s:10}]},{">li":[{i:"A41",s:22}]}],p:[{"":[{i:"A31"}]},{"":[{i:"A51"}]}],".ns-pot-share":[{"":[{i:"A61",f:1}]}],".ns_pot_search":[{"":[{i:"A71",f:3}]}]}],".ic_guide":[{"":[{"":[{i:"B11"}]}]}],".ntes_foot_link":[{"":[{"":[{i:"C11",f:1}]}]}]})},1e3)}();</script>
</body>
</html>
'''
