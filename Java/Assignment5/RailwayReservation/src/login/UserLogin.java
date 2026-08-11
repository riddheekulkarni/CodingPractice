package login;

public class UserLogin extends Login {
    @Override
    public boolean login(String username, String password) {
        return username.equals("user") && password.equals("1234");
    }
}
