Layout对于迅速的搭建界面和提高界面在不同分辨率的屏幕上的适应性具有很大的作用。这里简要介绍Android的Layout和研究一下它的实现。
Android有Layout：FrameLayout，LinearLayout，TableLayout，RelativeLayout，AbsoluteLayout。
放入Layout中进行排布的View的XML属性：
1.几种Layout中Item所共有的XML属性：
```  
(1)layout_width
(2)layout_height
(3)layout_marginLeft
(4)layout_marginTop
(5)layout_marginRight
(6)layout_marginBottom
(7)layout_gravity
FrameLayout是最简单的Layout，就只具有这些属性。
LinearLayout还会有：
(8)layout_weight
TableLayout的行TableRow是一个横向的（horizontal）的LinearLayout。
RelativeLayout有16个align相关的XML属性：
(9)layout_above
(10)layout_alignBaseline
(11)layout_alignBottom
(12)layout_alignLeft
(13)layout_alignParentBottom
(14)layout_alignParentLeft
(15)layout_alignParentRight
(16)layout_alignParentTop
(17)layout_alignRight
(18)layout_alignTop
(19)layout_below
(20)layout_centerHorizontal
(21)layout_centerInParent
(22)layout_centerVertical
(23)layout_toLeftOf
(24)layout_toRightOf
```
(1)和(2)用来确定放入Layout中的View的宽度和高度：它们的可能取值为fill_parent，wrap_content或者固定的像素值。
(3)(4)(5)(6)是放入Layout中的View期望它能够和Layout的边界或者其他View之间能够相距一段距离。
(7)用来确定View在Layout中的停靠位置。
(8)用于在LinearLayout中把所有子View排布之后的剩余空间按照它们的layout_weight分配给各个拥有这个属性的View。
(9)到(24)用来确定RelativeLayout中的View相对于Layout或者Layout中的其他View的位置。
根据Android的文档，Android会对Layou和View嵌套组成的这棵树进行2次遍历，一次是measure调用，用来确定Layout或者View的大小；一次是layout调用，用来确定Layout或者view的位置。当然后来我自己的山寨实现把这2次调用合并到了一起。那就是Layout在排布之前都对自己进行measure一次，然后对View递归调用Layout方法。这样子的大小肯定是确定了的。然后用确定了的大小来使用gravity或者align属性来定位，使用margin来调整位置。