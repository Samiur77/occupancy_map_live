# Deployment Guide for Occupancy Map

## Option 1: Render (Recommended - Free)

### Step 1: Prepare Your Repository
1. Push your code to GitHub/GitLab
2. Make sure you have these files in your repository:
   - `app.py`
   - `index.html`
   - `requirements.txt`
   - `render.yaml`

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` configuration
5. Set your environment variables:
   - `DB_DATABASE`: Your database name
   - `DB_UID`: Your database username
   - `DB_PWD`: Your database password
   - `DB_SERVER`: Your database server URL
6. Click "Create Web Service"
7. Your app will be available at: `https://your-app-name.onrender.com`

## Option 2: Railway (Alternative - Free Tier)

### Step 1: Deploy on Railway
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variables in the Railway dashboard
5. Deploy automatically

## Option 3: Heroku (Paid - $5/month minimum)

### Step 1: Install Heroku CLI
```bash
# Windows
# Download from: https://devcenter.heroku.com/articles/heroku-cli

# Or use winget
winget install --id=Heroku.HerokuCLI
```

### Step 2: Deploy
```bash
# Login to Heroku
heroku login

# Create a new Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set DB_DATABASE=your_database_name
heroku config:set DB_UID=your_username
heroku config:set DB_PWD=your_password
heroku config:set DB_SERVER=your_server_url

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

## Option 4: PythonAnywhere (Free Tier Available)

### Step 1: Sign up
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create a free account

### Step 2: Upload and Deploy
1. Upload your files via the Files tab
2. Open a Bash console and install dependencies:
   ```bash
   pip install --user -r requirements.txt
   ```
3. Create a new web app
4. Configure the WSGI file to point to your Flask app
5. Set environment variables in the web app configuration

## Important Notes

### Database Connection
⚠️ **Important**: Your current setup uses a local SQL Server database. For online deployment, you'll need:

1. **Cloud Database**: Use Azure SQL Database, AWS RDS, or similar
2. **Connection String**: Update your database connection to use the cloud database
3. **Firewall Rules**: Ensure your cloud database allows connections from your deployment platform

### Environment Variables
Make sure to set these in your deployment platform:
- `DB_DATABASE`: Database name
- `DB_UID`: Database username  
- `DB_PWD`: Database password
- `DB_SERVER`: Database server URL
- `DB_DRIVER`: ODBC Driver (usually "ODBC Driver 17 for SQL Server")

### Security Considerations
1. Never commit `.env` files to your repository
2. Use strong passwords for your database
3. Consider using connection pooling for better performance
4. Enable HTTPS on your deployment platform

## Quick Start with Render (Recommended)

1. **Fork/Clone this repository to GitHub**
2. **Sign up at [render.com](https://render.com)**
3. **Connect your GitHub repository**
4. **Set environment variables in Render dashboard**
5. **Deploy automatically**

Your app will be live at: `https://your-app-name.onrender.com`

## Troubleshooting

### Common Issues:
1. **Database Connection**: Ensure your cloud database is accessible
2. **Dependencies**: Check that all packages in `requirements.txt` are compatible
3. **Port Configuration**: Most platforms use port 5000 or 8000
4. **Environment Variables**: Double-check all database credentials

### Support:
- Render: [docs.render.com](https://docs.render.com)
- Railway: [docs.railway.app](https://docs.railway.app)
- Heroku: [devcenter.heroku.com](https://devcenter.heroku.com) 