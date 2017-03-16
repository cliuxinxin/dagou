<?php

namespace App\Http\Controllers;

use App\Group;
use Illuminate\Http\Request;

class GroupsController extends Controller
{
    public function index()
    {
        $items = Group::orderBy('name')->paginate(20);

        return view('group',compact('items'));
    }

    public function store()
    {
        Group::create(request(['name','detail','url']));

        return back();
    }
}
