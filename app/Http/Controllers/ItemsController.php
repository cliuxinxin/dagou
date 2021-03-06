<?php

namespace App\Http\Controllers;

use App\Item;
use Illuminate\Http\Request;

class ItemsController extends Controller
{
    //
    public function index()
    {
        $items = Item::orderBy('start_date', 'desc')->paginate(20);

        return view('index',compact('items'));
    }

    /**
     * Hostpital
     *
     * @return string
     */
    public function hospital()
    {
        $items = Item::hospital()->orderBy('start_date', 'desc')->paginate(20);

        return view('index',compact('items'));
    }

    public function apiIndex()
    {
        $items = Item::orderBy('start_date', 'desc')->paginate(20);

        return $items;
    }
}
