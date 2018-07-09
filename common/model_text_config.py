# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Params

def get_model_text(productModel):
    global text

    text = []

    if productModel == "OPPO":
        text = [ u'继续安装', u'安装', u'确认', u'打开', u'同意并继续']

    elif productModel == "Xiaomi":
        text =  [ u'安装', u'打开', u'允许', u'继续安装',u'退出']

    elif productModel == "samsung":
        text =  [ u'安装', u'打开', u'确认', u'继续安装']

    elif productModel == "360":
        text =  [ u'安装', u'打开', u'允许', u'android.widget.CheckBox', u'继续安装']

    elif productModel == "Lenovo":
        text =  [ u'安装', u'打开', u'下一步', u'继续安装']

    elif productModel == "vivo":
        text =  [ u'安装', u'打开', u'允许', u'继续安装']

    elif productModel == "gionee":
        text = [u'安装', u'打开', u'继续安装']

    elif productModel == "xlj":
        text = [u'继续', u'安装', u'打开', u'允许']

    elif productModel == "yunso":
        text = [u'继续', u'安装', u'打开', u'允许']

    elif productModel == "oysin":
        text = [u'继续', u'安装', u'打开', u'允许']

    elif productModel == "default":
        text =  [u'允许', u'Allow', u'确认', u'OK', u'安装', u'确定',
         u'继续', u'下一步', u'完成', u'同意', u'好', u'允许本次安装',
         u'备份我的数据', u'继续安装', u'Back up my data', u'同意并继续',
         u'我已充分了解该风险', u'继续安装', u'暂不删除', u'同意并安装',
         u'始终允许', u'替换', u'安装新程序', u'暂不处理', u'允许一次', u'重新安装']

    else:
        print("ParamError: Unknown model type, model should be [model]")

    return text
