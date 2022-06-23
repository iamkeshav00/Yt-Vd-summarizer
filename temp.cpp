#include<iostream>
#include<vector>
using namespace std;
 int findPivot(vector<int> nums)
        {
            int low=0;
            int high=nums.size()-1;
            while(low<high)
            {
                int mid=low+(high-low)/2;
                if(nums[mid]>=nums[0])
                {
                    low=mid+1;
                }else high=mid;
            }
            return low;
        }
    int binarySearch(vector<int> nums,int target,int low ,int high)
    {
        while(low<=high)
        {
            int mid=low+(high-low)/2;
            if(nums[mid]==target)return mid;
            else if(nums[mid]>target)high=mid-1;
            else low=mid+1;
        }
        return -1;
    }
    int search(vector<int>& nums, int target) {
        int pivot =findPivot(nums);
        if(target>=nums[pivot] && target <= nums[nums.size()-1])
        {
            return binarySearch(nums,target,pivot,nums.size()-1);
        }else
        {
            return binarySearch(nums,target,0,pivot-1);
        }
    }
int main(void)
{
    int n;
    cin>>n;
    vector<int> nums;
    for(int i=0;i<n;i++)
    {
        int temp;
        cin>>temp;
        nums.push_back(temp);

    }
    cout<<search(nums,0);
}