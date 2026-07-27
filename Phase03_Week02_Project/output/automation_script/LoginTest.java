package tests;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import pages.LoginPage;
import java.time.Duration;

public class LoginTest {
    private WebDriver driver;
    private LoginPage loginPage;

    @BeforeMethod
    public void setUp() {
        // TODO: Set system property for driver executable if needed
        driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.manage().window().maximize();
        driver.get("https://example.com/login"); // TODO: Replace with actual login URL
        loginPage = new LoginPage(driver);
    }

    @Test(priority = 1)
    public void verifySuccessfulLoginWithValidCredentials() {
        loginPage.login("validUser", "validPassword"); // TODO: Replace with actual valid credentials
        Assert.assertTrue(loginPage.isDashboardDisplayed(), "Dashboard is not displayed after successful login.");
    }

    @Test(priority = 2)
    public void verifyLoginFailsWithInvalidUsernameAndValidPassword() {
        loginPage.login("invalidUser", "validPassword"); // TODO: Replace with actual credentials
        String expectedError = "Invalid credentials"; // TODO: Replace with actual expected error message
        Assert.assertEquals(loginPage.getErrorMessage(), expectedError, "Error message mismatch for invalid username.");
    }

    @Test(priority = 3)
    public void verifyLoginFailsWithValidUsernameAndInvalidPassword() {
        loginPage.login("validUser", "invalidPassword"); // TODO: Replace with actual credentials
        String expectedError = "Invalid credentials"; // TODO: Replace with actual expected error message
        Assert.assertEquals(loginPage.getErrorMessage(), expectedError, "Error message mismatch for invalid password.");
    }

    @Test(priority = 4)
    public void verifyLoginFailsWhenUsernameFieldIsEmpty() {
        loginPage.login("", "validPassword");
        String expectedError = "Username is mandatory"; // TODO: Replace with actual expected error message
        Assert.assertEquals(loginPage.getErrorMessage(), expectedError, "Error message mismatch for empty username.");
    }

    @Test(priority = 5)
    public void verifyLoginFailsWhenPasswordFieldIsEmpty() {
        loginPage.login("validUser", "");
        String expectedError = "Password is mandatory"; // TODO: Replace with actual expected error message
        Assert.assertEquals(loginPage.getErrorMessage(), expectedError, "Error message mismatch for empty password.");
    }

    @Test(priority = 6)
    public void verifyLoginFailsWhenBothFieldsAreEmpty() {
        loginPage.login("", "");
        String expectedError = "Username and password are mandatory"; // TODO: Replace with actual expected error message
        Assert.assertEquals(loginPage.getErrorMessage(), expectedError, "Error message mismatch for both empty fields.");
    }

    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }
}