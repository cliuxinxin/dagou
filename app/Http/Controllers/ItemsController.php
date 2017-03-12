<?php

namespace App\Http\Controllers;

use App\Item;
use Illuminate\Http\Request;

class ItemsController extends Controller
{
    //
    public function index()
    {
        $items = Item::all();

        return view('index',compact('items'));
    }
}
