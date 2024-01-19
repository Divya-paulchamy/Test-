import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class MakeMyTripTest {
    WebDriver driver;
    @BeforeMethod
    public void setup() {

        System.setProperty("webdriver.chrome.driver", “C:\Users\DIVYA\Documents\selenium-bdd-cucumber-test\selenium-bdd-cucumber-test\Drivers");
        System.setProperty("webdriver.gecko.driver", “C:\Users\DIVYA\Documents\selenium-bdd-cucumber-test\selenium-bdd-cucumber-test\Drivers");
    }

    @Test(priority = 1)
    public void verifyMakeMyTripLogoFirefox() {
        driver = new FirefoxDriver();
        launchAndVerifyLogo(driver);
    }

    @Test(priority = 2)
    public void selectOneWayAndEnterLocationsChrome() {
        driver = new ChromeDriver();
        driver.get("https://www.makemytrip.com/");

        clickElement(driver, By.xpath("chNavIcon appendBottom2 chSprite chFlights active]"));
        clickElement(driver, By.xpath("/hsw_inputBox tripTypeWrapper"));

        enterText(driver, By.xpath("lbl_input latoBold font12 blueText appendBottom5"), "New Delhi");
        enterText(driver, By.xpath("lbl_input latoBold font12 blueText appendBottom5"), "Mumbai");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }

    }

    private void clickElement(WebDriver driver, By by) {
        WebElement element = driver.findElement(by);
        element.click();

    }

    private void enterText(WebDriver driver, By by, String text) {
        WebElement element = driver.findElement(by);
        element.clear();
        element.sendKeys(text);
    }

    private void launchAndVerifyLogo(WebDriver driver) {
        driver.get("https://www.makemytrip.com/");
        WebElement logoElement = driver.findElement(By.xpath("//imgak.mmtcdn.com/pwa_v3/pwa_hotel_assets/header/logo@2x.png"));
        Assert.assertTrue(logoElement.isDisplayed(), "MakeMyTrip logo is not present on the page.");
    }

}

 