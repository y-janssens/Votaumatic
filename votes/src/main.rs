use chrono::Local;
use headless_chrome::{Browser, LaunchOptions};
use std::error::Error;
use std::io::{Write, stdout};
use std::thread::sleep;
use std::time::Duration;

const ROOT: &str = "http://www.root-top.com/topsite";

const TOPSITES: &[&str] = &[
    "virtu4lgames/in.php?ID=6916",
    "obsession27/in.php?ID=27483",
    "gilgamesh/in.php?ID=8668",
    "justmarried/in.php?ID=1247",
    "melu/in.php?ID=5321",
    "pubrpgdesign/in.php?ID=347",
];

#[tokio::main]
async fn main() -> Result<(), Box<dyn Error>> {
    loop {
        session().await?;
        countdown(7500).await;
    }
}

async fn session() -> Result<(), Box<dyn Error>> {
    let options = LaunchOptions::default_builder()
        .headless(false)
        .window_size(Some((1920, 1080)))
        .build()?;

    let browser = Browser::new(options)?;

    for topsite_path in TOPSITES {
        let url = format!("{}/{}", ROOT, topsite_path);
        let now = Local::now().format("%d/%m/%Y %H:%M:%S");

        match vote(&browser, &url).await {
            Ok(_) => println!("{} : {} : Ok", now, url),
            Err(e) => println!("{} : {} : Erreur - {}", now, url, e),
        }
    }

    Ok(())
}

async fn vote(browser: &Browser, url: &str) -> Result<(), Box<dyn Error>> {
    let tab = browser.new_tab()?;
    tab.navigate_to(url)?;
    sleep(Duration::from_secs(2));
    tab.reload(true, None)?;
    sleep(Duration::from_secs(2));

    let button = tab.find_element("#BA")?;
    button.click()?;
    sleep(Duration::from_secs(2));

    tab.find_element(".action_OK")?;

    Ok(())
}

async fn countdown(seconds: u64) {
    let mut remaining = seconds;

    while remaining > 0 {
        let minutes = remaining / 60;
        let secs = remaining % 60;
        print!("\rProchain vote dans {:02}:{:02} minutes", minutes, secs);
        Write::flush(&mut stdout()).unwrap();

        sleep(Duration::from_secs(1));
        remaining -= 1;
    }
    println!();
}
