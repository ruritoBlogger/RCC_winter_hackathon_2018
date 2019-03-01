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
    val mode : Boolean = get_mode()
    var target_time : Int = get_time(mode)
    
    if(mode) target_time *= 60
    val start : Long = System.currentTimeMillis()
    var tmp : Double = (System.currentTimeMillis() - start).toDouble()

    while(true){
        //println("${((System.currentTimeMillis() - start)/1000).toDouble()} and ${target_time}")
        //if ( ((System.currentTimeMillis() - start)/1000).toDouble() > target_time ){
        if ( tmp/1000 > target_time ){
            println("設定した時間が経過しました")
            break
        }
        //else if (tmp != System.currentTimeMillis() - start - 0.2 || tmp/1000 != System.currentTimeMillis() - start + 0.2){
        //else if (tmp != ((System.currentTimeMillis() - start)/1000).toDouble()){
            //if(tmp != tmp2){
                //tmp2 = tmp
        println("%.2f".format(target_time.toDouble() - tmp/1000))
        tmp = (System.currentTimeMillis() - start).toDouble()
            //}
        //}
        //println("${(System.currentTimeMillis() - start)/1000}")
    }
}
