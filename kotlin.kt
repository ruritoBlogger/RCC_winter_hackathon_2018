fun get_mode() : Boolean {
    println("分単位もしくは秒単位どちらで計測しますか?(y or n)")
    var ans = readLine()
    if (ans == "y"){
        return true
    }else if (ans == "n"){
        return false
    }
    else
    {
        println("yもしくはnを入力してください")
        return get_mode()
    }
}

fun main(args: Array<String>){
    println("タイマーを起動しました")
    val mode = get_mode()
    println(mode)
}
