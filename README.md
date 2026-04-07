# Secure Remote Command Execution System

A client-server system that allows authenticated users to execute commands remotely using TCP sockets with built-in authentication and audit logging.

## Features

- **Client-Server Architecture**: TCP-based communication between client and server
- **Authentication System**: Username/password authentication with predefined users
- **Remote Command Execution**: Execute shell commands on the server remotely
- **Audit Logging**: All authentication attempts and command executions are logged
- **Secure Communication**: Basic security through authentication (note: for production use, consider TLS)

## Technologies

- Python 3.x
- Socket Programming (TCP)
- Subprocess for command execution
- Built-in logging for audit trails

## Prerequisites

- Python 3.6 or higher installed on both client and server machines
- Network connectivity between client and server

## Installation and Setup

### 1. Clone or Download the Project

Ensure you have the project files in a directory. The structure should be:

```
secure-remote-command/
├── README.md
├── client/
│   └── client.py
├── common/
│   └── protocol.py
└── server/
    ├── server.py
    ├── auth.py
    ├── logger.py
    ├── command_executor.py
    └── audit_log.txt
```

### 2. Server Setup

1. Navigate to the server directory:
   ```bash
   cd server
   ```

2. Ensure Python is installed:
   ```bash
   python --version
   ```

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

### 3. Client Setup

1. Navigate to the client directory:
   ```bash
   cd client
   ```

2. Ensure Python is installed (same as server).

## Usage

### Starting the Server

1. Open a terminal and navigate to the `server` directory.

2. Run the server:
   ```bash
   python server.py
   ```

   The server will start listening on `0.0.0.0:5000` and display:
   ```
   Server listening...
   ```

### Connecting with the Client

1. Open another terminal and navigate to the `client` directory.

2. Run the client:
   ```bash
   python client.py
   ```

3. When prompted, enter login credentials:
   - Username: `admin`, `user`, or `arayana`
   - Password: `1234`, `pass`, or `4567` respectively

4. If authentication succeeds, you'll see:
   ```
   Server response: AUTH_SUCCESS
   ```

5. Enter commands to execute on the server:
   ```
   Enter command: ls
   Enter command: pwd
   Enter command: echo "Hello World"
   ```

6. Type `exit` to disconnect:
   ```
   Enter command: exit
   ```

### Example Session

```
Username: admin
Password: 1234
Server response: AUTH_SUCCESS
Enter command: ls
Output:
README.md
client
common
server

Enter command: pwd
Output:
/path/to/secure-remote-command

Enter command: exit
```

## Security Notes

- **Default Credentials**: Change the hardcoded credentials in `server/auth.py` for production use.
- **Network Security**: This implementation uses plain TCP. For secure communication, consider adding TLS/SSL encryption.
- **Command Validation**: Currently allows all commands. Add command whitelisting for better security.
- **Logging**: Audit logs are stored in plain text. Consider secure logging practices.

## Implementation Details

### Server Components

- **`server.py`**: Main server loop handling connections, authentication, and command execution
- **`auth.py`**: Simple authentication module with hardcoded user credentials
- **`logger.py`**: Audit logging functionality
- **`command_executor.py`**: (Currently empty) Placeholder for advanced command execution logic

### Client Components

- **`client.py`**: Client application for connecting to server and sending commands

### Protocol

The system uses a simple text-based protocol:
- Authentication: `LOGIN <username> <password>`
- Commands: Raw command strings
- Responses: Command output or authentication status

### Architecture

1. Server binds to TCP port 5000 and listens for connections
2. Client connects and sends authentication request
3. Server validates credentials and responds with success/failure
4. On success, client can send commands which server executes via subprocess
5. All actions are logged to `audit_log.txt`

## Troubleshooting

### Connection Issues
- Ensure the server is running before starting the client
- Check firewall settings for port 5000
- Verify IP address in client.py matches server IP

### Authentication Failures
- Check username/password combinations in `server/auth.py`
- Ensure correct case sensitivity

### Command Execution Issues
- Some commands may not work as expected due to environment differences
- Check server logs in `audit_log.txt` for error details

## Future Enhancements

- Add TLS encryption for secure communication
- Implement user management (add/remove users)
- Add command whitelisting/blacklisting
- Support for file transfers
- Multi-client support with threading
- Configuration files for settings

## License

This project is for educational purposes. Use at your own risk.
