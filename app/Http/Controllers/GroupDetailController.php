<?php

namespace App\Http\Controllers;

use App\Group;
use App\GroupDetail;
use Illuminate\Http\Request;

class GroupDetailController extends Controller
{
    public function index($group)
    {
        $items = Group::find($group)->has('groupDetails')->orderBy('name')->paginate(20);

        dd(Group::find($group)->has('groupDetails'));

        return view('groupdetail',compact('items'));
    }


    public function store($group)
    {

        Group::find($group)->groupDetails()->create(request(['name','phone','address','detail']));

        return back();
    }
}
