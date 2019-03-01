fn get_mode() {
    print!("分単位もしくは秒単位どちらで計測しますか?(y or n)");
    
    let s = {
    let mut s = String::new(); // バッファを確保
    std::io::stdin().read_line(&mut s).unwrap(); // 一行読む。失敗を無視
    s.trim_right().to_owned() // 改行コードが末尾にくっついてくるので削る
    };
    if s == "y" {
        true;
    }else if s == "n" {
        false;
    } else { return get_mode(); }
}

fn main() {
    let mode = get_mode();
}
