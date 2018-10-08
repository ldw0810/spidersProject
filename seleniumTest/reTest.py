#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

htmlStr = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta name="renderer" content="webkit">
  <meta charset="UTF-8">
  <meta name="applicable-device" content="pc">
  <meta http-equiv="mobile-agent" content="format=html5; url=http://m.gufengmh.com/list/click/"/>
  <meta http-equiv="mobile-agent" content="format=xhtml; url=http://m.gufengmh.com/list/click/"/>
  <link rel="miphtml" href="http://m.gufengmh.com/list/click/">
  <meta name="csrf-param" content="_csrf">
  <meta name="csrf-token"
        content="sU8FPIyi_5yL7GrOyWMg6AsVhlxYPAp9-R3nieyWx4T2CDR0z5vI7r2HJomqBHaEWmLINwcPPR-oZYzI3cmU1Q==">
  <title>漫画列表-古风漫画网</title>
  <meta name="keyword" content="天才小毒妃漫画，大角虫漫画，王牌校草漫画，指染成婚漫画">
  <meta name="description"
        content="古风漫画网专注古风漫画，言情漫画，少女爱情等类型的漫画。古风漫画网第一时间更新天才小毒妃漫画，大角虫漫画，王牌校草漫画，指染成婚漫画等好看的漫画，看古风、少女爱情等类型漫画最好的网站！">
  <link href="/assets/988165a/css/font-awesome.min.css" rel="stylesheet">
  <link href="/assets/fb6fc4ca/css/bootstrap.css" rel="stylesheet">
  <link href="/plugins/toastr/toastr.min.css" rel="stylesheet">
  <link href="/css/main.css" rel="stylesheet">
  <link href="/assets/77151193/css/common.css" rel="stylesheet">
  <link href="/assets/77151193/css/base.css" rel="stylesheet">
  <link href="/assets/77151193/css/list.css" rel="stylesheet">
  <script src="/js/phone.js"></script>
  <script>;phone.check("http://m.gufengmh.com");</script>
</head>
<body class="clearfix">

<script>;var siteName = "";
var siteUrl = "http://www.gufengmh.com";</script>
<div class="topper">
  <div class="w998">
    <div class="fl">
      <a href="javascript:SinMH.addFavorite(siteUrl,siteName);">古风漫画网——古风言情的精选漫画网！</a>
    </div>
    <div class="user-area fr">
      <div class="user-view" id="history">
        <div class="handle">
          <a href="javascript:;">我的观看记录</a><i></i>
        </div>
        <div id="hListBox" class="panel shadow-gray">
          <div class="hlist" id="hList"></div>
          <div class="hlist-remove">
            <a id="hListClear" href="javascript:SinMH.clearHistory();">清空全部记录</a>
          </div>
        </div>
      </div>
      <div class="user-block user-action">
        <a href="/member/">会员中心</a></div>
      <div class="user-block user-action" id="update_notice">
        <a href="/member/unread/">更新通知</a> <em id="update_count" style="color: red;font-weight: 700;">0</em>
      </div>
      <div class="user-first user-login">
        <a href="/login/">【登录】</a> <a href="/register/">或【注册新账号】</a></div>
      <div class="user-first user-action">
        <img id="avatar" width="30px;"/><em id="username"></em>
        <a href="/logout/">【退出】</a>
      </div>
    </div>
  </div>
</div>
<div class="w998 mt10">
  <div class="header">
    <h1 class="logo fl">
      <a href="/"><img src="http://res.gufengmh.com/images/logo/logo.png" alt=""></a></h1>
    <div class="search fl">
      <fieldset>
        <input type="text" placeholder="请输入关键字..." class="keyword" id="keywords" lang="zh-CN"
               x-webkit-grammar="builtin:search" x-webkit-speech="" autocomplete="off"/>
        <input type="button" class="button" id="btnSearch" value="搜索"/>
      </fieldset>
      <div class="suggest" id="search-results">
      </div>
    </div>
    <div class="shortcuts fr">
      <a class="desktop" href="/member/subscribe/" rel="nofollow">我的订阅</a> <a
        href="javascript:SinMH.addFavorite(siteUrl,siteName);" class="favorite">加入收藏夹</a>
    </div>
  </div>
</div>
<div class="w998 nav-bar shadow">
  <div class="nav-sub fl" onmouseover="this.className='nav-sub nav-sub-over fl'"
       onmouseout="this.className='nav-sub fl'">
    <h2>漫画大全导航</h2>
    <div class="nav-sub-cont-bg">
      <div class="nav-sub-cont">
        <div id="w2" class="filter clearfix">
          <div class="filter-header clearfix">
            <div class="filter-title">漫画大全 - 分类筛选</div>
            <ul class="filter-click">
              <li class="filter-clear"><a class="filter-link-clear" href="/list/">重新筛选</a></li>
            </ul>
          </div>
          <div class="filter-nav clearfix">
            <div class="filter-item clearfix"><label>按类型</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/shaonian/">少年漫画</a></li>
                <li><a class="" href="/list/shaonv/">少女漫画</a></li>
                <li><a class="" href="/list/qingnian/">青年漫画</a></li>
                <li><a class="" href="/list/zhenrenmanhua/">真人漫画</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按地区</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/ribenmanhua/">日本漫画</a></li>
                <li><a class="" href="/list/guochanmanhua/">国产漫画</a></li>
                <li><a class="" href="/list/gangtaimanhua/">港台漫画</a></li>
                <li><a class="" href="/list/oumeimanhua/">欧美漫画</a></li>
                <li><a class="" href="/list/hanguomanhua/">韩国漫画</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按剧情</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/maoxian/">冒险</a></li>
                <li><a class="" href="/list/mofa/">魔法</a></li>
                <li><a class="" href="/list/kehuan/">科幻</a></li>
                <li><a class="" href="/list/kongbu/">恐怖</a></li>
                <li><a class="" href="/list/lishi/">历史</a></li>
                <li><a class="" href="/list/jingji/">竞技</a></li>
                <li><a class="" href="/list/huanlexiang/">欢乐向</a></li>
                <li><a class="" href="/list/xifangmohuan/">西方魔幻</a></li>
                <li><a class="" href="/list/aiqing/">爱情</a></li>
                <li><a class="" href="/list/xuanyi/">悬疑</a></li>
                <li><a class="" href="/list/qihuan/">奇幻</a></li>
                <li><a class="" href="/list/qingxiaoshuo/">轻小说</a></li>
                <li><a class="" href="/list/sige/">四格</a></li>
                <li><a class="" href="/list/shengui/">神鬼</a></li>
                <li><a class="" href="/list/zhiyu/">治愈</a></li>
                <li><a class="" href="/list/xiaoyuan/">校园</a></li>
                <li><a class="" href="/list/weiniang/">伪娘</a></li>
                <li><a class="" href="/list/danmei/">耽美</a></li>
                <li><a class="" href="/list/hougong/">后宫</a></li>
                <li><a class="" href="/list/mohuan/">魔幻</a></li>
                <li><a class="" href="/list/wuxia/">武侠</a></li>
                <li><a class="" href="/list/zhichang/">职场</a></li>
                <li><a class="" href="/list/zhentan/">侦探</a></li>
                <li><a class="" href="/list/meishi/">美食</a></li>
                <li><a class="" href="/list/gedou/">格斗</a></li>
                <li><a class="" href="/list/lizhi/">励志</a></li>
                <li><a class="" href="/list/yinyuewudao/">音乐舞蹈</a></li>
                <li><a class="" href="/list/rexue/">热血</a></li>
                <li><a class="" href="/list/zhanzheng/">战争</a></li>
                <li><a class="" href="/list/gaoxiao/">搞笑</a></li>
                <li><a class="" href="/list/shenghuo/">生活</a></li>
                <li><a class="" href="/list/baihe/">百合</a></li>
                <li><a class="" href="/list/mengji/">萌系</a></li>
                <li><a class="" href="/list/jiecao/">节操</a></li>
                <li><a class="" href="/list/xingzhuanhuan/">性转换</a></li>
                <li><a class="" href="/list/yanyi/">颜艺</a></li>
                <li><a class="" href="/list/gufeng/">古风</a></li>
                <li><a class="" href="/list/xianxia/">仙侠</a></li>
                <li><a class="" href="/list/zhaiji/">宅系</a></li>
                <li><a class="" href="/list/juqing/">剧情</a></li>
                <li><a class="" href="/list/shenmo/">神魔</a></li>
                <li><a class="" href="/list/xuanhuan/">玄幻</a></li>
                <li><a class="" href="/list/chuanyue/">穿越</a></li>
                <li><a class="" href="/list/qita/">其他</a></li>
                <li><a class="" href="/list/huanxiang/">幻想</a></li>
                <li><a class="" href="/list/motong/">墨瞳</a></li>
                <li><a class="" href="/list/maimeng/">麦萌</a></li>
                <li><a class="" href="/list/manman/">漫漫</a></li>
                <li><a class="" href="/list/manhuadao/">漫画岛</a></li>
                <li><a class="" href="/list/tuili/">推理</a></li>
                <li><a class="" href="/list/dongfang/">东方</a></li>
                <li><a class="" href="/list/kuaikan/">快看</a></li>
                <li><a class="" href="/list/jizhan/">机战</a></li>
                <li><a class="" href="/list/gaoqingdanxing/">高清单行</a></li>
                <li><a class="" href="/list/xinzuo/">新作</a></li>
                <li><a class="" href="/list/tougao/">投稿</a></li>
                <li><a class="" href="/list/richang/">日常</a></li>
                <li><a class="" href="/list/shougong/">手工</a></li>
                <li><a class="" href="/list/yundong/">运动</a></li>
                <li><a class="" href="/list/weimei/">唯美</a></li>
                <li><a class="" href="/list/dushi/">都市</a></li>
                <li><a class="" href="/list/jingxian/">惊险</a></li>
                <li><a class="" href="/list/jiangshi/">僵尸</a></li>
                <li><a class="" href="/list/lianai/">恋爱</a></li>
                <li><a class="" href="/list/nuexin/">虐心</a></li>
                <li><a class="" href="/list/chunai/">纯爱</a></li>
                <li><a class="" href="/list/fuchou/">复仇</a></li>
                <li><a class="" href="/list/dongzuo/">动作</a></li>
                <li><a class="" href="/list/qita2/">其它</a></li>
                <li><a class="" href="/list/egao/">恶搞</a></li>
                <li><a class="" href="/list/mingxing/">明星</a></li>
                <li><a class="" href="/list/zhenhan/">震撼</a></li>
                <li><a class="" href="/list/anhei/">暗黑</a></li>
                <li><a class="" href="/list/naodong/">脑洞</a></li>
                <li><a class="" href="/list/xuexing/">血腥</a></li>
                <li><a class="" href="/list/youyaoqi/">有妖气</a></li>
                <li><a class="" href="/list/jijia/">机甲</a></li>
                <li><a class="" href="/list/qingchun/">青春</a></li>
                <li><a class="" href="/list/lingyi/">灵异</a></li>
                <li><a class="" href="/list/tongren/">同人</a></li>
                <li><a class="" href="/list/langman/">浪漫</a></li>
                <li><a class="" href="/list/quanmou/">权谋</a></li>
                <li><a class="" href="/list/shehui/">社会</a></li>
                <li><a class="" href="/list/gongdou/">宫斗</a></li>
                <li><a class="" href="/list/baoxiao/">爆笑</a></li>
                <li><a class="" href="/list/tiyu/">体育</a></li>
                <li><a class="" href="/list/lanmu/">栏目</a></li>
                <li><a class="" href="/list/caihong/">彩虹</a></li>
                <li><a class="" href="/list/zhentantuili/">侦探推理</a></li>
                <li><a class="" href="/list/shaonuaiqing/">少女爱情</a></li>
                <li><a class="" href="/list/gaoxiaoxiju/">搞笑喜剧</a></li>
                <li><a class="" href="/list/kongbulingyi/">恐怖灵异</a></li>
                <li><a class="" href="/list/kehuanmohuan/">科幻魔幻</a></li>
                <li><a class="" href="/list/jingjitiyu/">竞技体育</a></li>
                <li><a class="" href="/list/wuxiagedou/">武侠格斗</a></li>
                <li><a class="" href="/list/jianniang/">舰娘</a></li>
                <li><a class="" href="/list/danmeiBL/">耽美BL</a></li>
                <li><a class="" href="/list/xiee/">邪恶</a></li>
                <li><a class="" href="/list/zongheqita/">综合其它</a></li>
                <li><a class="" href="/list/qingnian/">青年</a></li>
                <li><a class="" href="/list/zhainan/">宅男</a></li>
                <li><a class="" href="/list/zazhi/">杂志</a></li>
                <li><a class="" href="/list/yinyue/">音乐</a></li>
                <li><a class="" href="/list/quancai/">全彩</a></li>
                <li><a class="" href="/list/heidao/">黑道</a></li>
                <li><a class="" href="/list/lianaidanmei/">恋爱耽美</a></li>
                <li><a class="" href="/list/rexuemaoxian/">热血冒险</a></li>
                <li><a class="" href="/list/funv/">腐女</a></li>
                <li><a class="" href="/list/gushi/">故事</a></li>
                <li><a class="" href="/list/shaonv/">少女</a></li>
                <li><a class="" href="/list/zongcai/">总裁</a></li>
                <li><a class="" href="/list/baoxiaoxiju/">爆笑喜剧</a></li>
                <li><a class="" href="/list/qitamanhua/">其他漫画</a></li>
                <li><a class="" href="/list/lianaishenghuo/">恋爱生活</a></li>
                <li><a class="" href="/list/kongbuxuanyi/">恐怖悬疑</a></li>
                <li><a class="" href="/list/danmeirensheng/">耽美人生</a></li>
                <li><a class="" href="/list/chongwu/">宠物</a></li>
                <li><a class="" href="/list/zhandou/">战斗</a></li>
                <li><a class="" href="/list/zhaohuanshou/">召唤兽</a></li>
                <li><a class="" href="/list/yineng/">异能</a></li>
                <li><a class="" href="/list/zhuangbi/">装逼</a></li>
                <li><a class="" href="/list/yishijie/">异世界</a></li>
                <li><a class="" href="/list/zhengju/">正剧</a></li>
                <li><a class="" href="/list/wenxin/">温馨</a></li>
                <li><a class="" href="/list/jingqi/">惊奇</a></li>
                <li><a class="" href="/list/jiakong/">架空</a></li>
                <li><a class="" href="/list/qingsong/">轻松</a></li>
                <li><a class="" href="/list/weilai/">未来</a></li>
                <li><a class="" href="/list/keji/">科技</a></li>
                <li><a class="" href="/list/shaonao/">烧脑</a></li>
                <li><a class="" href="/list/gaoxiaoegao/">搞笑恶搞</a></li>
                <li><a class="" href="/list/mhuaquan/">mhuaquan</a></li>
                <li><a class="" href="/list/shaonian/">少年</a></li>
                <li><a class="" href="/list/sigeduoge/">四格多格</a></li>
                <li><a class="" href="/list/bazong/">霸总</a></li>
                <li><a class="" href="/list/xiuzhen/">修真</a></li>
                <li><a class="" href="/list/gushimanhua/">故事漫画</a></li>
                <li><a class="" href="/list/huiben/">绘本</a></li>
                <li><a class="" href="/list/youxi/">游戏</a></li>
                <li><a class="" href="/list/zhenren/">真人</a></li>
                <li><a class="" href="/list/jingsong/">惊悚</a></li>
                <li><a class="" href="/list/manhua/">漫画</a></li>
                <li><a class="" href="/list/weizhongquan/">微众圈</a></li>
                <li><a class="" href="/list/yujie/">御姐</a></li>
                <li><a class="" href="/list/xiaoshuogaibian/">小说改编</a></li>
                <li><a class="" href="/list/luoli/">萝莉</a></li>
                <li><a class="" href="/list/1024manhua/">1024manhua</a></li>
                <li><a class="" href="/list/jiating/">家庭</a></li>
                <li><a class="" href="/list/shenhua/">神话</a></li>
                <li><a class="" href="/list/shishi/">史诗</a></li>
                <li><a class="" href="/list/moshi/">末世</a></li>
                <li><a class="" href="/list/yulequan/">娱乐圈</a></li>
                <li><a class="" href="/list/gandong/">感动</a></li>
                <li><a class="" href="/list/lunli/">伦理</a></li>
                <li><a class="" href="/list/zazhiquanben/">杂志全本</a></li>
                <li><a class="" href="/list/zhiyu2/">致郁</a></li>
                <li><a class="" href="/list/shangzhan/">商战</a></li>
                <li><a class="" href="/list/zhupu/">主仆</a></li>
                <li><a class="" href="/list/manhuaquan/">漫画圈</a></li>
                <li><a class="" href="/list/lianaijuqingmanhua/">恋爱、剧情漫画</a></li>
                <li><a class="" href="/list/hunai/">婚爱</a></li>
                <li><a class="" href="/list/haomen/">豪门</a></li>
                <li><a class="" href="/list/neihan/">内涵</a></li>
                <li><a class="" href="/list/xingzhuan/">性转</a></li>
                <li><a class="" href="/list/xiangcun/">乡村</a></li>
                <li><a class="" href="/list/gongting/">宫廷</a></li>
                <li><a class="" href="/list/duanzi/">段子</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按字母</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/a/">A</a></li>
                <li><a class="" href="/list/b/">B</a></li>
                <li><a class="" href="/list/c/">C</a></li>
                <li><a class="" href="/list/d/">D</a></li>
                <li><a class="" href="/list/e/">E</a></li>
                <li><a class="" href="/list/f/">F</a></li>
                <li><a class="" href="/list/g/">G</a></li>
                <li><a class="" href="/list/h/">H</a></li>
                <li><a class="" href="/list/i/">I</a></li>
                <li><a class="" href="/list/j/">J</a></li>
                <li><a class="" href="/list/k/">K</a></li>
                <li><a class="" href="/list/l/">L</a></li>
                <li><a class="" href="/list/m/">M</a></li>
                <li><a class="" href="/list/n/">N</a></li>
                <li><a class="" href="/list/o/">O</a></li>
                <li><a class="" href="/list/p/">P</a></li>
                <li><a class="" href="/list/q/">Q</a></li>
                <li><a class="" href="/list/r/">R</a></li>
                <li><a class="" href="/list/s/">S</a></li>
                <li><a class="" href="/list/t/">T</a></li>
                <li><a class="" href="/list/u/">U</a></li>
                <li><a class="" href="/list/v/">V</a></li>
                <li><a class="" href="/list/w/">W</a></li>
                <li><a class="" href="/list/x/">X</a></li>
                <li><a class="" href="/list/y/">Y</a></li>
                <li><a class="" href="/list/z/">Z</a></li>
                <li><a class="" href="/list/1/">其他</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按进度</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/wanjie/">已完结</a></li>
                <li><a class="" href="/list/lianzai/">连载中</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="nav-main fl">

    <ul>
      <li class="first">
        <a class="" href="/">首页</a></li>
      <li>
        <a class="" href="/update/">最新更新</a></li>
      <li>
        <a class="" href="/rank/">排行榜</a></li>
      <li>
        <a class="" href="/list/guochanmanhua/">国产漫画</a></li>
      <li>
        <a class="" href="/list/ribenmanhua/">日本漫画</a></li>
      <li class="laster">
        <a class="hover" href="/list/">漫画大全</a></li>
    </ul>
  </div>
  <div class="nav-less fl">
    <a id="randomView" href="/comic/random/">漫画随心看</a></div>
</div>

<div class="wrap">
  <div class="page-main">
    <div class="w998 mt10">
      <div class="box-gray shadow-gray">
        <div id="w0" class="filter clearfix">
          <div class="filter-header bar-title clearfix">
            <div class="filter-title">漫画大全 - 分类筛选</div>
            <ul class="filter-click">
              <li class="filter-clear"><a class="filter-link-clear" href="/list/">重新筛选</a></li>
            </ul>
          </div>
          <div class="filter-nav clearfix">
            <div class="filter-item clearfix"><label>按类型</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/shaonian/">少年漫画</a></li>
                <li><a class="" href="/list/shaonv/">少女漫画</a></li>
                <li><a class="" href="/list/qingnian/">青年漫画</a></li>
                <li><a class="" href="/list/zhenrenmanhua/">真人漫画</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按地区</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/ribenmanhua/">日本漫画</a></li>
                <li><a class="" href="/list/guochanmanhua/">国产漫画</a></li>
                <li><a class="" href="/list/gangtaimanhua/">港台漫画</a></li>
                <li><a class="" href="/list/oumeimanhua/">欧美漫画</a></li>
                <li><a class="" href="/list/hanguomanhua/">韩国漫画</a></li>
              </ul>
            </div>
            2018-10-07 20:35:38 [scrapy.core.engine] INFO: Closing spider (finished)
            <div class="filter-item clearfix"><label>按剧情</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/maoxian/">冒险</a></li>
                <li><a class="" href="/list/mofa/">魔法</a></li>
                <li><a class="" href="/list/kehuan/">科幻</a></li>
                <li><a class="" href="/list/kongbu/">恐怖</a></li>
                <li><a class="" href="/list/lishi/">历史</a></li>
                <li><a class="" href="/list/jingji/">竞技</a></li>
                <li><a class="" href="/list/huanlexiang/">欢乐向</a></li>
                <li><a class="" href="/list/xifangmohuan/">西方魔幻</a></li>
                <li><a class="" href="/list/aiqing/">爱情</a></li>
                <li><a class="" href="/list/xuanyi/">悬疑</a></li>
                <li><a class="" href="/list/qihuan/">奇幻</a></li>
                <li><a class="" href="/list/qingxiaoshuo/">轻小说</a></li>
                <li><a class="" href="/list/sige/">四格</a></li>
                <li><a class="" href="/list/shengui/">神鬼</a></li>
                <li><a class="" href="/list/zhiyu/">治愈</a></li>
                <li><a class="" href="/list/xiaoyuan/">校园</a></li>
                <li><a class="" href="/list/weiniang/">伪娘</a></li>
                <li><a class="" href="/list/danmei/">耽美</a></li>
                <li><a class="" href="/list/hougong/">后宫</a></li>
                <li><a class="" href="/list/mohuan/">魔幻</a></li>
                <li><a class="" href="/list/wuxia/">武侠</a></li>
                <li><a class="" href="/list/zhichang/">职场</a></li>
                <li><a class="" href="/list/zhentan/">侦探</a></li>
                <li><a class="" href="/list/meishi/">美食</a></li>
                <li><a class="" href="/list/gedou/">格斗</a></li>
                <li><a class="" href="/list/lizhi/">励志</a></li>
                <li><a class="" href="/list/yinyuewudao/">音乐舞蹈</a></li>
                <li><a class="" href="/list/rexue/">热血</a></li>
                <li><a class="" href="/list/zhanzheng/">战争</a></li>
                <li><a class="" href="/list/gaoxiao/">搞笑</a></li>
                <li><a class="" href="/list/shenghuo/">生活</a></li>
                <li><a class="" href="/list/baihe/">百合</a></li>
                <li><a class="" href="/list/mengji/">萌系</a></li>
                <li><a class="" href="/list/jiecao/">节操</a></li>
                <li><a class="" href="/list/xingzhuanhuan/">性转换</a></li>
                <li><a class="" href="/list/yanyi/">颜艺</a></li>
                <li><a class="" href="/list/gufeng/">古风</a></li>
                <li><a class="" href="/list/xianxia/">仙侠</a></li>
                <li><a class="" href="/list/zhaiji/">宅系</a></li>
                <li><a class="" href="/list/juqing/">剧情</a></li>
                <li><a class="" href="/list/shenmo/">神魔</a></li>
                <li><a class="" href="/list/xuanhuan/">玄幻</a></li>
                <li><a class="" href="/list/chuanyue/">穿越</a></li>
                <li><a class="" href="/list/qita/">其他</a></li>
                <li><a class="" href="/list/huanxiang/">幻想</a></li>
                <li><a class="" href="/list/motong/">墨瞳</a></li>
                <li><a class="" href="/list/maimeng/">麦萌</a></li>
                <li><a class="" href="/list/manman/">漫漫</a></li>
                <li><a class="" href="/list/manhuadao/">漫画岛</a></li>
                <li><a class="" href="/list/tuili/">推理</a></li>
                <li><a class="" href="/list/dongfang/">东方</a></li>
                <li><a class="" href="/list/kuaikan/">快看</a></li>
                <li><a class="" href="/list/jizhan/">机战</a></li>
                <li><a class="" href="/list/gaoqingdanxing/">高清单行</a></li>
                <li><a class="" href="/list/xinzuo/">新作</a></li>
                <li><a class="" href="/list/tougao/">投稿</a></li>
                <li><a class="" href="/list/richang/">日常</a></li>
                <li><a class="" href="/list/shougong/">手工</a></li>
                <li><a class="" href="/list/yundong/">运动</a></li>
                <li><a class="" href="/list/weimei/">唯美</a></li>
                <li><a class="" href="/list/dushi/">都市</a></li>
                <li><a class="" href="/list/jingxian/">惊险</a></li>
                <li><a class="" href="/list/jiangshi/">僵尸</a></li>
                <li><a class="" href="/list/lianai/">恋爱</a></li>
                <li><a class="" href="/list/nuexin/">虐心</a></li>
                <li><a class="" href="/list/chunai/">纯爱</a></li>
                <li><a class="" href="/list/fuchou/">复仇</a></li>
                <li><a class="" href="/list/dongzuo/">动作</a></li>
                <li><a class="" href="/list/qita2/">其它</a></li>
                <li><a class="" href="/list/egao/">恶搞</a></li>
                <li><a class="" href="/list/mingxing/">明星</a></li>
                <li><a class="" href="/list/zhenhan/">震撼</a></li>
                <li><a class="" href="/list/anhei/">暗黑</a></li>
                <li><a class="" href="/list/naodong/">脑洞</a></li>
                <li><a class="" href="/list/xuexing/">血腥</a></li>
                <li><a class="" href="/list/youyaoqi/">有妖气</a></li>
                <li><a class="" href="/list/jijia/">机甲</a></li>
                <li><a class="" href="/list/qingchun/">青春</a></li>
                <li><a class="" href="/list/lingyi/">灵异</a></li>
                <li><a class="" href="/list/tongren/">同人</a></li>
                <li><a class="" href="/list/langman/">浪漫</a></li>
                <li><a class="" href="/list/quanmou/">权谋</a></li>
                <li><a class="" href="/list/shehui/">社会</a></li>
                <li><a class="" href="/list/gongdou/">宫斗</a></li>
                <li><a class="" href="/list/baoxiao/">爆笑</a></li>
                <li><a class="" href="/list/tiyu/">体育</a></li>
                <li><a class="" href="/list/lanmu/">栏目</a></li>
                <li><a class="" href="/list/caihong/">彩虹</a></li>
                <li><a class="" href="/list/zhentantuili/">侦探推理</a></li>
                <li><a class="" href="/list/shaonuaiqing/">少女爱情</a></li>
                <li><a class="" href="/list/gaoxiaoxiju/">搞笑喜剧</a></li>
                <li><a class="" href="/list/kongbulingyi/">恐怖灵异</a></li>
                <li><a class="" href="/list/kehuanmohuan/">科幻魔幻</a></li>
                <li><a class="" href="/list/jingjitiyu/">竞技体育</a></li>
                <li><a class="" href="/list/wuxiagedou/">武侠格斗</a></li>
                <li><a class="" href="/list/jianniang/">舰娘</a></li>
                <li><a class="" href="/list/danmeiBL/">耽美BL</a></li>
                <li><a class="" href="/list/xiee/">邪恶</a></li>
                <li><a class="" href="/list/zongheqita/">综合其它</a></li>
                <li><a class="" href="/list/qingnian/">青年</a></li>
                <li><a class="" href="/list/zhainan/">宅男</a></li>
                <li><a class="" href="/list/zazhi/">杂志</a></li>
                <li><a class="" href="/list/yinyue/">音乐</a></li>
                <li><a class="" href="/list/quancai/">全彩</a></li>
                <li><a class="" href="/list/heidao/">黑道</a></li>
                <li><a class="" href="/list/lianaidanmei/">恋爱耽美</a></li>
                <li><a class="" href="/list/rexuemaoxian/">热血冒险</a></li>
                <li><a class="" href="/list/funv/">腐女</a></li>
                <li><a class="" href="/list/gushi/">故事</a></li>
                <li><a class="" href="/list/shaonv/">少女</a></li>
                <li><a class="" href="/list/zongcai/">总裁</a></li>
                <li><a class="" href="/list/baoxiaoxiju/">爆笑喜剧</a></li>
                <li><a class="" href="/list/qitamanhua/">其他漫画</a></li>
                <li><a class="" href="/list/lianaishenghuo/">恋爱生活</a></li>
                <li><a class="" href="/list/kongbuxuanyi/">恐怖悬疑</a></li>
                <li><a class="" href="/list/danmeirensheng/">耽美人生</a></li>
                <li><a class="" href="/list/chongwu/">宠物</a></li>
                <li><a class="" href="/list/zhandou/">战斗</a></li>
                <li><a class="" href="/list/zhaohuanshou/">召唤兽</a></li>
                <li><a class="" href="/list/yineng/">异能</a></li>
                <li><a class="" href="/list/zhuangbi/">装逼</a></li>
                <li><a class="" href="/list/yishijie/">异世界</a></li>
                <li><a class="" href="/list/zhengju/">正剧</a></li>
                <li><a class="" href="/list/wenxin/">温馨</a></li>
                <li><a class="" href="/list/jingqi/">惊奇</a></li>
                <li><a class="" href="/list/jiakong/">架空</a></li>
                <li><a class="" href="/list/qingsong/">轻松</a></li>
                <li><a class="" href="/list/weilai/">未来</a></li>
                <li><a class="" href="/list/keji/">科技</a></li>
                <li><a class="" href="/list/shaonao/">烧脑</a></li>
                <li><a class="" href="/list/gaoxiaoegao/">搞笑恶搞</a></li>
                <li><a class="" href="/list/mhuaquan/">mhuaquan</a></li>
                <li><a class="" href="/list/shaonian/">少年</a></li>
                <li><a class="" href="/list/sigeduoge/">四格多格</a></li>
                <li><a class="" href="/list/bazong/">霸总</a></li>
                <li><a class="" href="/list/xiuzhen/">修真</a></li>
                <li><a class="" href="/list/gushimanhua/">故事漫画</a></li>
                <li><a class="" href="/list/huiben/">绘本</a></li>
                <li><a class="" href="/list/youxi/">游戏</a></li>
                <li><a class="" href="/list/zhenren/">真人</a></li>
                <li><a class="" href="/list/jingsong/">惊悚</a></li>
                <li><a class="" href="/list/manhua/">漫画</a></li>
                <li><a class="" href="/list/weizhongquan/">微众圈</a></li>
                <li><a class="" href="/list/yujie/">御姐</a></li>
                <li><a class="" href="/list/xiaoshuogaibian/">小说改编</a></li>
                <li><a class="" href="/list/luoli/">萝莉</a></li>
                <li><a class="" href="/list/1024manhua/">1024manhua</a></li>
                <li><a class="" href="/list/jiating/">家庭</a></li>
                <li><a class="" href="/list/shenhua/">神话</a></li>
                <li><a class="" href="/list/shishi/">史诗</a></li>
                <li><a class="" href="/list/moshi/">末世</a></li>
                <li><a class="" href="/list/yulequan/">娱乐圈</a></li>
                <li><a class="" href="/list/gandong/">感动</a></li>
                <li><a class="" href="/list/lunli/">伦理</a></li>
                <li><a class="" href="/list/zazhiquanben/">杂志全本</a></li>
                <li><a class="" href="/list/zhiyu2/">致郁</a></li>
                <li><a class="" href="/list/shangzhan/">商战</a></li>
                <li><a class="" href="/list/zhupu/">主仆</a></li>
                <li><a class="" href="/list/manhuaquan/">漫画圈</a></li>
                <li><a class="" href="/list/lianaijuqingmanhua/">恋爱、剧情漫画</a></li>
                <li><a class="" href="/list/hunai/">婚爱</a></li>
                <li><a class="" href="/list/haomen/">豪门</a></li>
                <li><a class="" href="/list/neihan/">内涵</a></li>
                <li><a class="" href="/list/xingzhuan/">性转</a></li>
                <li><a class="" href="/list/xiangcun/">乡村</a></li>
                <li><a class="" href="/list/gongting/">宫廷</a></li>
                <li><a class="" href="/list/duanzi/">段子</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按字母</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/a/">A</a></li>
                <li><a class="" href="/list/b/">B</a></li>
                <li><a class="" href="/list/c/">C</a></li>
                <li><a class="" href="/list/d/">D</a></li>
                <li><a class="" href="/list/e/">E</a></li>
                <li><a class="" href="/list/f/">F</a></li>
                <li><a class="" href="/list/g/">G</a></li>
                <li><a class="" href="/list/h/">H</a></li>
                <li><a class="" href="/list/i/">I</a></li>
                <li><a class="" href="/list/j/">J</a></li>
                <li><a class="" href="/list/k/">K</a></li>
                <li><a class="" href="/list/l/">L</a></li>
                <li><a class="" href="/list/m/">M</a></li>
                <li><a class="" href="/list/n/">N</a></li>
                <li><a class="" href="/list/o/">O</a></li>
                <li><a class="" href="/list/p/">P</a></li>
                <li><a class="" href="/list/q/">Q</a></li>
                <li><a class="" href="/list/r/">R</a></li>
                <li><a class="" href="/list/s/">S</a></li>
                <li><a class="" href="/list/t/">T</a></li>
                <li><a class="" href="/list/u/">U</a></li>
                <li><a class="" href="/list/v/">V</a></li>
                <li><a class="" href="/list/w/">W</a></li>
                <li><a class="" href="/list/x/">X</a></li>
                <li><a class="" href="/list/y/">Y</a></li>
                <li><a class="" href="/list/z/">Z</a></li>
                <li><a class="" href="/list/1/">其他</a></li>
              </ul>
            </div>
            <div class="filter-item clearfix"><label>按进度</label>
              <ul>
                <li><a class="active" href="/list/">全部</a></li>
                <li><a class="" href="/list/wanjie/">已完结</a></li>
                <li><a class="" href="/list/lianzai/">连载中</a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w998 mt16 cf">
      <div class="bar-tab book-sort">
        <h5 class="fl"><strong>排序方式</strong></h5>
        <div class="fl">
          <ul class="orderby">
            <li><a href="/list/post/?page=1" data-sort="post">按发布排序</a></li>
            <li><a href="/list/update/?page=1" data-sort="update">按更新排序</a></li>
            <li><a class="asc" href="/list/-click/?page=1" data-sort="-click">按点击排序</a></li>
          </ul>
        </div>
      </div>
      <div id="w1" class="">
        <ul class='book-list clearfix' id='contList'>
          <li class="item-lg" data-key="81"><a class="cover" href="http://www.gufengmh.com/manhua/bailianchengshen/"
                                               title="百炼成神">
            <img src="http://res.gufengmh.com/images/cover/201807/1530935442Y6Tc2lgwA6XJPVum.jpg" alt="百炼成神"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第286话 黔驴技穷</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/bailianchengshen/">百炼成神</a></p>
            <span class="updateon">更新于：2018-10-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="208"><a class="cover" href="http://www.gufengmh.com/manhua/haomentianjiaqianqi/"
                                                title="豪门天价前妻">
            <img src="http://res.gufengmh.com/images/cover/201807/1530857356t-FxI-3kbyYxjf-G.jpg" alt="豪门天价前妻"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至80话 后续章节</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/haomentianjiaqianqi/">豪门天价前妻</a></p>
            <span class="updateon">更新于：2018-10-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="259"><a class="cover" href="http://www.gufengmh.com/manhua/baqingeshao/"
                                                title="霸情恶少：调教小逃妻">
            <img src="http://res.gufengmh.com/images/cover/201807/1530949991cgdHnxOXcSZVZRUp.jpg" alt="霸情恶少：调教小逃妻"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至阴谋</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/baqingeshao/">霸情恶少：调教小逃妻</a></p>
            <span class="updateon">更新于：2018-10-06    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="262"><a class="cover" href="http://www.gufengmh.com/manhua/zhiranchenghun/"
                                                title="指染成婚">
            <img src="http://res.gufengmh.com/images/cover/201807/1530949981xfQxKWuOsP1F_aHr.jpg" alt="指染成婚"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至盛装的你</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/zhiranchenghun/">指染成婚</a></p>
            <span class="updateon">更新于：2018-10-06    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7142"><a class="cover" href="http://www.gufengmh.com/manhua/wanjiexianzong/"
                                                 title="万界仙踪">
            <img src="http://res.gufengmh.com/images/cover/201807/1530974701znvnTTgQHuTGmlSw.jpg" alt="万界仙踪"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第110话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/wanjiexianzong/">万界仙踪</a></p>
            <span class="updateon">更新于：2018-10-02    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="255"><a class="cover"
                                                href="http://www.gufengmh.com/manhua/sanshengsanshishilitaohua/"
                                                title="三生三世 十里桃花">
            <img src="http://res.gufengmh.com/images/cover/201807/1530974716snq9AbEzjTo-Lo_A.jpg" alt="三生三世 十里桃花"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至106 【番外篇一】（上）</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/sanshengsanshishilitaohua/">三生三世 十里桃花</a></p>
            <span class="updateon">更新于：2018-09-10    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="2876"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/reshangshouxizongcai/"
                                                 title="惹上首席总裁">
            <img src="http://res.gufengmh.com/images/cover/201807/1530857195fegmg7ELL2vArO34.jpg" alt="惹上首席总裁"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第133话</span>
            <span class="fd"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/reshangshouxizongcai/">惹上首席总裁</a></p>
            <span class="updateon">更新于：2018-08-23    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7453"><a class="cover" href="http://www.gufengmh.com/manhua/jiemoren/"
                                                 title="戒魔人">
            <img src="http://res.gufengmh.com/images/cover/201807/1530949978BtwvyRkEbES0ERAc.jpg" alt="戒魔人"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第402话 神秘大咖</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/jiemoren/">戒魔人</a></p>
            <span class="updateon">更新于：2018-10-04    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="3375"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/chongshenghaomenzhiqiangshiguilai/"
                                                 title="重生豪门之强势归来">
            <img src="http://res.gufengmh.com/images/cover/201807/1530846585AC-BEx9tF1OE2MFA.jpg" alt="重生豪门之强势归来"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第171话 一时失言</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/chongshenghaomenzhiqiangshiguilai/">重生豪门之强势归来</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7551"><a class="cover" href="http://www.gufengmh.com/manhua/lanchi/" title="蓝翅">
            <img src="http://res.gufengmh.com/images/cover/201807/1530925711XXUN5pNB63TnanGh.jpg" alt="蓝翅"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第89话圆谎04</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/lanchi/">蓝翅</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="6995"><a class="cover" href="http://www.gufengmh.com/manhua/huyaoxiaohongniang/"
                                                 title="狐妖小红娘">
            <img src="http://res.gufengmh.com/images/cover/201807/1530974703dgMcaLte-RagYVYT.jpg" alt="狐妖小红娘"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至总302·涂山实力</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/huyaoxiaohongniang/">狐妖小红娘</a></p>
            <span class="updateon">更新于：2018-09-30    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="8313"><a class="cover" href="http://www.gufengmh.com/manhua/wuliandianfeng/"
                                                 title="武炼巅峰">
            <img src="http://res.gufengmh.com/images/cover/201807/1530507928Ce8ARSYdUE7q7uGJ.jpg" alt="武炼巅峰"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至88.真正的传承之地</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/wuliandianfeng/">武炼巅峰</a></p>
            <span class="updateon">更新于：2018-10-06    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="3607"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/dihaolaogongtaikuangre/"
                                                 title="帝豪老公太狂热">
            <img src="http://res.gufengmh.com/images/cover/201703/1490014005SXWwyrDHoN78I9sM.jpg" alt="帝豪老公太狂热"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第58话 让你，爬上我的床</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/dihaolaogongtaikuangre/">帝豪老公太狂热</a></p>
            <span class="updateon">更新于：2017-11-09    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="4903"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/zongcaideqiyueqingren/"
                                                 title="总裁的契约情人">
            <img src="http://res.gufengmh.com/images/cover/201807/1530949998dVznefEO5OpV6QSV.jpg" alt="总裁的契约情人"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至他是我爸爸？</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/zongcaideqiyueqingren/">总裁的契约情人</a></p>
            <span class="updateon">更新于：2018-07-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="202"><a class="cover"
                                                href="http://www.gufengmh.com/manhua/badaozongcaiaishangwodajiao/"
                                                title="霸道总裁爱上我">
            <img src="http://res.gufengmh.com/images/cover/201806/1528568203AajEAzqbeZjyy_BF.jpg" alt="霸道总裁爱上我"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至新年快乐</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/badaozongcaiaishangwodajiao/">霸道总裁爱上我</a></p>
            <span class="updateon">更新于：2018-05-19    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="292"><a class="cover" href="http://www.gufengmh.com/manhua/jipinlamahaoV/"
                                                title="极品辣妈好V5">
            <img src="http://res.gufengmh.com/images/cover/201806/1529630609cJL7SlKkHLLWCE_R.jpg" alt="极品辣妈好V5"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第51话 后续章节</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/jipinlamahaoV/">极品辣妈好V5</a></p>
            <span class="updateon">更新于：2018-06-22    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7757"><a class="cover" href="http://www.gufengmh.com/manhua/woweicangsheng/"
                                                 title="我为苍生">
            <img src="http://res.gufengmh.com/images/cover/201807/1530950927pKJMfMU_ROV0uaht.jpg" alt="我为苍生"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至公告：国庆快乐！</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/woweicangsheng/">我为苍生</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="5213"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/bujiazongcaijiananpu/"
                                                 title="不嫁总裁嫁男仆">
            <img src="http://res.gufengmh.com/images/cover/201807/15307994343GMN9Yj7npkk76rD.jpg" alt="不嫁总裁嫁男仆"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第131话 隔墙有耳</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/bujiazongcaijiananpu/">不嫁总裁嫁男仆</a></p>
            <span class="updateon">更新于：2018-09-30    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="3339"><a class="cover" href="http://www.gufengmh.com/manhua/jjbjzcxmwf/"
                                                 title="拒绝暴君专宠：凶猛王妃">
            <img src="http://res.gufengmh.com/images/cover/201807/1530925713TZWapgV1ygR-kJmm.jpg" alt="拒绝暴君专宠：凶猛王妃"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至131 诀别</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/jjbjzcxmwf/">拒绝暴君专宠：凶猛王妃</a></p>
            <span class="updateon">更新于：2018-07-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="207"><a class="cover" href="http://www.gufengmh.com/manhua/wangpaixiaocao/"
                                                title="王牌校草">
            <img src="http://res.gufengmh.com/images/cover/201807/1530857317jS6JvD8m0jwFB7mt.jpg" alt="王牌校草"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第234话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/wangpaixiaocao/">王牌校草</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="9579"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/zhongshengzhidushixiuxian/"
                                                 title="重生之都市修仙">
            <img src="http://res.gufengmh.com/images/cover/201807/1530732793-IwshyvahVVD_d7Z.jpg" alt="重生之都市修仙"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第八十九话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/zhongshengzhidushixiuxian/">重生之都市修仙</a></p>
            <span class="updateon">更新于：2018-10-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="1067"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/jushuowoshiwangdenuer/"
                                                 title="据说我是王的女儿？">
            <img src="http://res.gufengmh.com/images/cover/201807/1530855975eDhtO23i0FwEhS9a.jpg" alt="据说我是王的女儿？"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至310.治愈大家的力量</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/jushuowoshiwangdenuer/">据说我是王的女儿？</a></p>
            <span class="updateon">更新于：2018-10-06    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="287"><a class="cover" href="http://www.gufengmh.com/manhua/douluodalu/"
                                                title="斗罗大陆">
            <img src="http://res.gufengmh.com/images/cover/201807/1530537387O-NvKf3ZohGRjv6E.jpg" alt="斗罗大陆"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第208话 对话紫珍珠（2）</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/douluodalu/">斗罗大陆</a></p>
            <span class="updateon">更新于：2018-09-26    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7090"><a class="cover" href="http://www.gufengmh.com/manhua/yuanzun/"
                                                 title="元尊">
            <img src="http://res.gufengmh.com/images/cover/201807/15309746941ARTdkhAe91e3_Lp.jpg" alt="元尊"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第82话：杂鱼（下）</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/yuanzun/">元尊</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="8430"><a class="cover" href="http://www.gufengmh.com/manhua/heisesiyecao/"
                                                 title="黑色四叶草">
            <img src="http://res.gufengmh.com/images/cover/201807/1530537395llI164vK5JVemPNe.jpg" alt="黑色四叶草"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第174话 飞来</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/heisesiyecao/">黑色四叶草</a></p>
            <span class="updateon">更新于：2018-09-22    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7947"><a class="cover" href="http://www.gufengmh.com/manhua/wangpaiyushi/"
                                                 title="王牌御史">
            <img src="http://res.gufengmh.com/images/cover/201807/1530893049MP-1JOiRV10D3NwV.jpg" alt="王牌御史"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至404,你们是怎么吻的？</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/wangpaiyushi/">王牌御史</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="205"><a class="cover"
                                                href="http://www.gufengmh.com/manhua/xingmengouxiangjihua/"
                                                title="星梦偶像计划">
            <img src="http://res.gufengmh.com/images/cover/201807/1530950914EUORo9wv0ym0zysp.jpg" alt="星梦偶像计划"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第241话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/xingmengouxiangjihua/">星梦偶像计划</a></p>
            <span class="updateon">更新于：2018-07-26    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="3212"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/jinmishuzenmeturanzheyang/"
                                                 title="金助理怎么突然这样">
            <img src="http://res.gufengmh.com/images/cover/201807/1530848700nLHYLUAUxP0v6mle.jpg" alt="金助理怎么突然这样"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至烦恼的父亲</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/jinmishuzenmeturanzheyang/">金助理怎么突然这样</a></p>
            <span class="updateon">更新于：2018-07-20    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="4237"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/shouwangdezhuanchong/"
                                                 title="兽王的专宠">
            <img src="http://res.gufengmh.com/images/cover/201807/1530925706Pn20xd61nNqKmS-d.jpg" alt="兽王的专宠"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第112话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/shouwangdezhuanchong/">兽王的专宠</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7693"><a class="cover" href="http://www.gufengmh.com/manhua/shanhainizhan/"
                                                 title="山海逆战">
            <img src="http://res.gufengmh.com/images/cover/201807/1530974708TaCBpSi6HX60MWSx.jpg" alt="山海逆战"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至大决战（下）</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/shanhainizhan/">山海逆战</a></p>
            2018-10-07 20:35:38 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
            {'downloader/request_bytes': 458,
            'downloader/request_count': 2,
            'downloader/request_method_count/GET': 2,
            'downloader/response_bytes': 11162,
            'downloader/response_count': 2,
            'downloader/response_status_count/200': 2,
            'finish_reason': 'finished',
            'finish_time': datetime.datetime(2018, 10, 7, 12, 35, 38, 229771),
            'log_count/DEBUG': 3,
            'log_count/INFO': 7,
            'memusage/max': 62099456,
            'memusage/startup': 62099456,
            'response_received_count': 2,
            'scheduler/dequeued': 1,
            'scheduler/dequeued/memory': 1,
            'scheduler/enqueued': 1,
            'scheduler/enqueued/memory': 1,
            'start_time': datetime.datetime(2018, 10, 7, 12, 35, 37, 900062)}
            2018-10-07 20:35:38 [scrapy.core.engine] INFO: Spider closed (finished)
            <span class="updateon">更新于：2018-10-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="578"><a class="cover" href="http://www.gufengmh.com/manhua/fenglintianxia/"
                                                title="凤临天下-王妃十三岁">
            <img src="http://res.gufengmh.com/images/cover/201712/1512226923-yUngG0B_FppkAS1.jpg" alt="凤临天下-王妃十三岁"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第四季 012 下</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/fenglintianxia/">凤临天下-王妃十三岁</a></p>
            <span class="updateon">更新于：2018-07-25    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="5850"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/congqianyouzuolingjianshan/"
                                                 title="从前有座灵剑山">
            <img src="http://res.gufengmh.com/images/cover/201807/1530720446De91mS36LiwI-pnp.jpg" alt="从前有座灵剑山"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第三百八十八话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/congqianyouzuolingjianshan/">从前有座灵剑山</a></p>
            <span class="updateon">更新于：2018-10-07    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="4011"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/wangjuedesiyoubaobei/"
                                                 title="王爵的私有宝贝">
            <img src="http://res.gufengmh.com/images/cover/201807/1530846600btWMLwAys0Q3WRmM.jpg" alt="王爵的私有宝贝"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第一百五十六话</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/wangjuedesiyoubaobei/">王爵的私有宝贝</a></p>
            <span class="updateon">更新于：2018-10-05    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="440"><a class="cover" href="http://www.gufengmh.com/manhua/fengnitianxia/"
                                                title="凤逆天下">
            <img src="http://res.gufengmh.com/images/cover/201708/1503690118VUhhGSrXYSXUCSrL.jpg" alt="凤逆天下"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第93话 生死谜团（5）下</span>
            <span class="fd"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/fengnitianxia/">凤逆天下</a></p>
            <span class="updateon">更新于：2018-09-21    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="7452"><a class="cover" href="http://www.gufengmh.com/manhua/xinwangqiuwangzi/"
                                                 title="新网球王子">
            <img src="http://res.gufengmh.com/images/cover/201807/1530949976LH4xsKIbQyeB92Sg.jpg" alt="新网球王子"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第243话 送运动型饮料的小人儿</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/xinwangqiuwangzi/">新网球王子</a></p>
            <span class="updateon">更新于：2018-06-04    <em>1.0</em>
</span></li>
          <li class="item-lg" data-key="6734"><a class="cover"
                                                 href="http://www.gufengmh.com/manhua/huanghouniangniangdewumaotexiao/"
                                                 title="皇后娘娘的五毛特效">
            <img src="http://res.gufengmh.com/images/cover/201807/1530949994SUea3kMNEDetcKgY.jpg" alt="皇后娘娘的五毛特效"
                 default="images/default/cover.png"> <span class="bg"></span>
            <span class="tt">更新至第一百话 危机重重</span>
            <span class="sl"></span>
          </a>
            <p class="ell"><a href="http://www.gufengmh.com/manhua/huanghouniangniangdewumaotexiao/">皇后娘娘的五毛特效</a></p>
            <span class="updateon">更新于：2018-10-06    <em>1.0</em>
</span></li>
        </ul>
        <div class='page-container'>
          <ul class="pagination">
            <li class="first disabled"><span>第一页</span></li>
            <li class="prev disabled"><span>上一页</span></li>
            <li class="active"><a href="/list/click/?page=1" data-page="0">1</a></li>
            <li><a href="/list/click/?page=2" data-page="1">2</a></li>
            <li><a href="/list/click/?page=3" data-page="2">3</a></li>
            <li><a href="/list/click/?page=4" data-page="3">4</a></li>
            <li><a href="/list/click/?page=5" data-page="4">5</a></li>
            <li><a href="/list/click/?page=6" data-page="5">6</a></li>
            <li><a href="/list/click/?page=7" data-page="6">7</a></li>
            <li><a href="/list/click/?page=8" data-page="7">8</a></li>
            <li><a href="/list/click/?page=9" data-page="8">9</a></li>
            <li><a href="/list/click/?page=10" data-page="9">10</a></li>
            <li class="next"><a href="/list/click/?page=2" data-page="1">下一页</a></li>
            <li class="last"><a href="/list/click/?page=362" data-page="361">末页</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
<!-- 版权{ -->
<div class="footer mt16 cf">
  <div class="footer-wrap">
    <div class="footer-cont">
      <p>
        古风漫画网为非赢利性质的公益网站。所有漫画均来自网络，本站转载旨在宣传和推广优秀的漫画作品，以便漫画爱好者研究漫画技巧和构图方式。若喜欢，请购买正版书籍以支持作者！漫画版权归原漫画作者及发行商所有。如有侵犯到您的权益，请联系我们，确认之后立即删除。本站不负任何相关责任！
      </p>
      <p>联系邮箱：2649388396@QQ.com <em>/</em> Copyright © 2016 <em>/</em> GuFengMH.Com <em>/</em> All Rights Reserved
        <em>/</em> <a href="/">古风漫画网</a> <em>/</em> 蜀ICP备16035243号-1 </p>
    </div>
  </div>
</div>

<!-- }版权 -->
<div class="t_j" style="display: none">
  <script src="http://www.gufengmh.com/assets/t_j/tongji.js"></script>
</div>
<div class="scroll-top"><a href="javascript:SinMH.scrollTo(0);" id="backTop" title="返回顶部">回到顶部</a></div>

<div class="modal fade" tabindex="-1" role="dialog" aria-labelledby="alert-modal" id="alert-modal">
  <div class="modal-dialog modal-sm">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">×</span>
        </button>
        <h4 class="modal-title">提示信息</h4>
      </div>
      <div class="modal-body text-center"> 弹窗内容</div>
      <div class="modal-footer text-center" style="text-align: center;">
        <button type="button" class="btn btn-primary" data-dismiss="modal" aria-label="Close">确 &nbsp; 定
        </button>
      </div>
    </div>
  </div>
</div>
<div class="modal fade" tabindex="-1" role="dialog" aria-labelledby="confirm-modal" id="confirm-modal">
  <div class="modal-dialog modal-sm">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">×</span>
        </button>
        <h4 class="modal-title">提示信息</h4>
      </div>
      <div class="modal-body text-center"> 弹窗内容</div>
      <div class="modal-footer text-center" style="text-align: center;">
        <button type="button" class="btn btn-primary btn-confirm" data-dismiss="modal" aria-label="Confirm">确
          &nbsp; 定
        </button>
        <button type="button" class="btn btn-default" data-dismiss="modal" aria-label="Close">取 &nbsp; 消
        </button>
      </div>
    </div>
  </div>
</div>
<div style="display:none"></div>

<script id="search-template" type="text/html">
  <%if(items&&items.length>0){%>
  <%for(var i = 0; i
  <items.length;i++){
  var item = items[i];
  %>
  <li title="<%=item.title%>" data-url="<%= item.uri %>">
        <span class="pull-right">更新至：
        <a href="<%= item.uri+ item.last_chapter_id%>.html"><%=item.last_chapter_name%></a></span>
    [<a href="/author/id-<%= item.author_id %>/"><%=item.author%></a>]
    <a href="<%= item.uri %>"><%=item.title%></a>
    [<span class="<%=item.serialise==1?'text-danger':'text-success'%>"><%=item.serialise==1?'连载中':'已完结'%></span>]

  </li>
  <%}%>
  <%}else{%>
  <li>暂无搜索结果</li>
  <%}%>
</script>
<script id="history-template" type="text/html">
  <%if(list&&list.length>0){%>
  <ul>
    <%for(var i = 0; i < list.length;i++){
    var item = list[i];
    %>
    <li>
      <a class="hdel fr" title="删除" rel="<%=item.comic_id%>"
         href="javascript:SinMH.removeHistory(<%=item.comic_id%>)"><span>删除</span></a>
      <a class="book" href="<%=item.comic_url%>"><%=item.comic_name%></a> <em>[</em>
      <a href="<%=item.read_chapter_url%>" class="red"><%=item.read_chapter%></a> <em>]</em>
      <div>
        <span class="fr"><a href="<%=item.read_chapter_url%>#p=<%=item.read_page%>">继续观看</a></span>
        <span class="htime">上次于 <%= filter.asDateTime(item.read_at)%> 观看</span>
      </div>
    </li>
    <%}%>
  </ul>
  <%}else{%>
  暂无历史纪录
  <%}%>
</script>

<script src="/assets/3b2647fc/jquery.js"></script>
<script src="/assets/1fb7938e/yii.js"></script>
<script src="/assets/fb6fc4ca/js/bootstrap.js"></script>
<script src="/plugins/toastr/toastr.min.js"></script>
<script src="/plugins/baiduTemplate.js"></script>
<script src="/plugins/jquery/jquery.cookie.js"></script>
<script src="/plugins/jquery/jquery.image.js"></script>
<script src="/plugins/jquery/jquery.lazyload.min.js"></script>
<script src="/plugins/jquery/jquery.hotkeys.js"></script>
<script src="/plugins/bootstrap/bootstrap.hover.dropdown.js"></script>
<script src="/plugins/bootstrap/bootstrap.hover.tab.js"></script>
<script src="/js/config.js"></script>
<script src="/js/common.js"></script>
<script src="/assets/77151193/js/theme.js"></script>
<script>jQuery(function ($) {
  ;SinMH.init();
  SinTheme.init();
  $("img").lazyload();
  ;
});</script>
</body>
</html>
'''
print htmlStr
print re.findall(r'(?<=<li class="item-lg").*?(?=li)', htmlStr, re.M)

if __name__ == '__main__':
    print re.search(r'\d{4}-\d{2}-\d{2}', htmlStr).group(0)
