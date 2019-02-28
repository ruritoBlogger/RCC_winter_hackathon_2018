fun get_mode() : Boolean {
    print("分単位もしくは秒単位どちらで計測しますか?(y or n)")
    val ans = readLine()
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

fun get_time(mode : Boolean) : Int {
    if (mode) print("設定したい時間を入力してください(分):")
    else print("設定したい時間を入力してください(秒):")
    
    try{
        val input : Int = Integer.parseInt(readLine())
        return input
    }
    catch(e : java.lang.NumberFormatException){
        println("時間を入力してください")
        return get_time(mode)
    }
}

fun main(args: Array<String>){
    println("タイマーを起動しました")
    val mode = get_mode()
    val target_time = get_time(mode)
    println(target_time)
}
