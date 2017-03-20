<?php

namespace App\Http\Controllers;

use App\Scrap;
use Illuminate\Http\Request;

class ScrapController extends Controller
{
    //
    public function index()
    {
        $items = Scrap::orderBy('insert_numbers','desc')->paginate(20);

        return view('scrape',compact('items'));
    }

}
