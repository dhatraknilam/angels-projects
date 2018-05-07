void findsum(TreeNode* root, vector<vector<int> >& ans, int sum, vector<int>& path){
    if(sum == 0 && root->left == NULL && root->right == NULL){
        ans.push_back(path);
    }
    
    if(root->left != NULL){
        path.push_back((root->left)->val);
        findsum(root->left, ans, sum - (root->left)->val, path);
        path.pop_back();
    }
    
    if(root->right != NULL){
        path.push_back((root->right)->val);
        findsum(root->right, ans, sum - (root->right)->val, path);
        path.pop_back();
    }
    
}

vector<vector<int> > Solution::pathSum(TreeNode* root, int sum) {
   
    vector<vector<int> > ans;
    vector<int> path;
    
    if(root == NULL){
        return ans;
    }
    
    path.push_back(root->val);
    
    findsum(root, ans, sum - root->val, path);
    
    return ans;
}