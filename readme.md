## Carvekit background remover for AWS Lambda docker image
Lambda version [https://github.com/OPHoperHPO/image-background-remove-tool](https://github.com/OPHoperHPO/image-background-remove-tool)

## Usage
1. Build and push the image to ECR
```
docker build --target=lambda -t YOUR_ECR_REPOSIRY_NAME --push .
```
2. Create Lambda function and select the image as Lambda image source.
3. Choose deploy type:
  - RBAC invoke are default entry. Invoke with event data:
```json
{
  "data": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADRCAYAAACXSM1..."
}
```
  - Function URL: modify the CMD to `lambda.function_url_invoke`. `POST` image data base64 in body:
```json
{
  "data": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMYAAADRCAYAAACXSM1..."
}
```
  - Flask webserver (Override both entrypoint and cmd).
