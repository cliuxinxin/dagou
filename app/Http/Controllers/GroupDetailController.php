<?php

namespace App\Http\Controllers;

use App\Group;
use App\GroupDetail;
use Illuminate\Http\Request;

class GroupDetailController extends Controller
{
    public function index($group)
    {
        $group = Group::find($group);

        $items = $group->groupDetails()->Oldest()->paginate(20);

        return view('groupdetail',compact('items','group'));
    }


    public function store($group)
    {

        Group::find($group)->groupDetails()->create(request(['name','phone','address','detail']));

        return back();
    }
}
